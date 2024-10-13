# django
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # вход в дамин панель
    path("admin/", admin.site.urls),
    path("myapp/", include("myapp.urls", namespace="myapp")),
]

# добаляем к нашим основным url-путям пути к нами медиа файлам
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
