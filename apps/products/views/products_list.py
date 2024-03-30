from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.products.models import Products
from apps.products.serializers import ProductSerializer


class ProductsListAPIView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer