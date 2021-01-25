from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # раздел администратора
    path("admin/", admin.site.urls),
    # импорт правил из приложения posts
    path("", include("link.urls")),
    path("", include("api.urls")),
    # регистрация и авторизация
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
]
