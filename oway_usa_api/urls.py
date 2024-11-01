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
    path("notifications/", include("apps.notifications.urls")),
    path("categories/", include("apps.categories.urls")),
    path("catalog/sites/", include("apps.catalog_sites.urls")),
    path("products/", include("apps.products.urls")),
    path("billing/", include("apps.billing.urls")),
    path("add_user_for_admin/", include("apps.add_user_in_ap.urls")),
    path("purchase/", include("apps.purchase.urls")),
    path("countries/", include("apps.countries.urls")),
    path("cities/", include("apps.cities.urls")),
    path("warehouses/", include("apps.warehouses.urls")),
    path("statics/", include("apps.statics.urls")),
    path("my_warehouse/", include("apps.my_warehouse.urls")),
    path("logos/", include("apps.logos.urls")),
    path("otside_of_illinois/", include("apps.clients_outside_of_illinois.urls")),
    path("cargos/", include("apps.cargos.urls")),
    path("items/", include("apps.items.urls")),
    path("contacts/", include("apps.contacts.urls")),
    path("address/", include("apps.address.urls")),
]

urlpatterns = [
    path('api/', include(api_urls)),
]

urlpatterns += doc_url

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
