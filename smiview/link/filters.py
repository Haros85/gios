import django_filters
from .models import News


class NewsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = News
        fields = ["pub_date"]
