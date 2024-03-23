from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from oway_usa_api.yasg import urlpatterns as doc_url

django_urls = [
    path('admin/', admin.site.urls),
]

api_urls = [
    path("django/", include(django_urls)),
    path("users/", include("apps.users.urls")),
    path("categories/", include("apps.categories.urls")),
]

urlpatterns = [
    path('api/', include(api_urls)),
]

urlpatterns += doc_url

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
