# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'apps.users.apps.UsersConfig',
    'apps.notifications.apps.NotificationsConfig',
    'apps.categories.apps.CategoriesConfig',
    'apps.catalog_sites.apps.CatalogSitesConfig',
    'apps.products.apps.ProductsConfig',
    'apps.billing.apps.BillingConfig',
    'apps.add_user_in_ap.apps.AddUserInApConfig',
    'apps.purchase.apps.PurchaseConfig',
    'apps.countries.apps.CountriesConfig',
    'apps.warehouses.apps.WarehousesConfig',
    'apps.tracking.apps.TrackingConfig',
]

INSTALLED_APPS = [
    *DJANGO_APPS,
    *MY_APPS,
    'rest_framework',
    'corsheaders',
    'drf_yasg',
]