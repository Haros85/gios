from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_link/", views.add_link, name="add_link"),
    path("<int:news_id>/edit/", views.edit_link, name="edit_link"),
    path("<int:news_id>/delete/", views.delete_link, name="del_link"),
    path("filter/", views.FilterNewsView.as_view(), name="filter"),
    path("export/", views.export_csv, name="export_csv"),
]