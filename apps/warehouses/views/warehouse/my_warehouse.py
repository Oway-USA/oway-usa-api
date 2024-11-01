from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.warehouses.models import WarehouseProduct
from apps.warehouses.serializers import WarehouseProductListSerializer


class MyWarehouseListAPI(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_unique_id_user(self):
        user_unique_id = self.request.user.unique_id
        return user_unique_id

    def get_serializer_class(self):
        return WarehouseProductListSerializer

    def get_queryset(self):
        return WarehouseProduct.objects.filter(unique_id_user=self.get_unique_id_user())

    @swagger_auto_schema(
        operation_summary="My Warehouse List",
        responses={
            200: WarehouseProductListSerializer(many=True)
        }
    )
    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)