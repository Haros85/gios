from django.conf.urls import url
from django.contrib import admin

from .views import ChartData


urlpatterns = [
    url(r"^api/chart/data/$", ChartData.as_view()),
]
