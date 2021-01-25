from django.forms import ModelForm
from link.models import News
from django_select2.forms import Select2Widget, Select2MultipleWidget

class NewsForm(ModelForm):
    class Meta:
            model = News
            fields = ['pub_date', 'smi', 'name', 'url', 'keywords', 'age', 'news_type', 'departments',]
            widgets = {
                'smi': Select2Widget,
                'news_type': Select2Widget,
                'keywords': Select2MultipleWidget,
                'departments': Select2MultipleWidget,
            }