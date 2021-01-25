import csv

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Q, Count
from .models import News, Smi
from .forms import NewsForm
from django.contrib.auth.decorators import login_required
import datetime as dt
from datetime import datetime
from django.views.generic import ListView


class FilterData:
    """Данные для фильтра"""

    def get_smi(self):
        return Smi.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


@login_required
def index(request):
    now = dt.datetime.now().date()
    latest = News.objects.filter(pub_date=now)
    return render(request, "index.html", {"news": latest})


@login_required
def dashboard(request):
    ystd = (dt.datetime.now() - dt.timedelta(days=1)).date()
    week = (dt.datetime.now() - dt.timedelta(days=7)).date()
    td_news = News.objects.filter(pub_date=dt.datetime.now()).count()
    ystd_news = News.objects.filter(pub_date=ystd).count()
    week_news = News.objects.filter(pub_date__gte=week).count()
    month_news = News.objects.filter(pub_date__month=dt.datetime.now().month).count()
    old_month_news = News.objects.filter(
        pub_date__month=(dt.datetime.now().month - 1)
    ).count()
    year_news = News.objects.filter(pub_date__year=dt.datetime.now().year).count()
    old_year_news = News.objects.filter(
        pub_date__year=(dt.datetime.now().year - 1)
    ).count()
    all_news = News.objects.count()
    stats = {
        "за сегодня": td_news,
        "за вчера": ystd_news,
        "за неделю": week_news,
        "с начала месяца": month_news,
        "прошлый месяц": old_month_news,
        "с начала года": year_news,
        "прошлый год": old_year_news,
        "всего в базе": all_news,
    }
    values = News.objects.values("smi__name").annotate(link_count=Count("id"))
    lables = []
    data = []
    for item in values:
        lables.append(item["smi__name"])
        data.append(item["link_count"])
    return render(
        request, "dashboard.html", {"lables": lables, "data": data, "stats": stats}
    )


@login_required
def add_link(request):
    if request.method == "POST":
        form = NewsForm(request.POST or None)
        if form.is_valid():
            link = form.save(commit=False)
            link.save()
            form.save_m2m()
            return redirect("index")
    form = NewsForm()
    return render(request, "new_link.html", {"form": form})


@login_required
def edit_link(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    form = NewsForm(request.POST or None, instance=news)
    if request.method == "POST":
        if form.is_valid():
            link = form.save(commit=False)
            link.save()
            form.save_m2m()
            return redirect("index")

    return render(request, "new_link.html", {"form": form, "news": news})


@login_required
def delete_link(request, news_id):
    news = News.objects.filter(id=news_id)
    news.delete()
    return redirect("index")


class FilterNewsView(FilterData, ListView):
    """Результат фильтра"""

    def get_queryset(self):
        queryset = News.objects.filter(
            Q(smi__in=self.request.GET.getlist("smi_id")),
            Q(pub_date__in=self.request.GET.getlist("pub_date")),
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        smi = []
        smi_values = self.request.GET.getlist("smi_id")
        for val in smi_values:
            smi.append(int(val))
        context["smi"] = smi
        date = dt.datetime.strptime(self.request.GET.get("pub_date"), "%Y-%m-%d").date()
        context["date"] = date
        return context


@login_required
def export_csv(request):
    from io import StringIO

    file = StringIO()
    date = request.GET.get("date")
    writer = csv.writer(file, delimiter=";")
    writer.writerow(
        [
            "Дата",
            "СМИ",
            "Новость",
            "Ссылка",
            "Ключевые слова",
            "Дети",
            "Категория новостей",
            "Тип СМИ",
            "Служба",
        ]
    )

    news = News.objects.filter(Q(pub_date=date)).values_list(
        "pub_date",
        "smi__name",
        "name",
        "url",
        "keywords__name",
        "age",
        "news_type__name",
        "smi__type_smi__name",
        "departments__name",
    )
    for item in news:
        writer.writerow(item)

    response = HttpResponse(file.getvalue().encode("cp1251"), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="export.csv"'

    return response
