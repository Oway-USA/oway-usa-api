from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from apps.add_user_in_ap.serialiers import AddUserSerializer
from apps.users.models import User, PassportFront, PassportBack
from apps.users.serializers import ProfileSerializer
from apps.shared.views.list_view import ListAPIView


class AddUserForAdminAPIView(APIView):
    serializer_class = AddUserSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = User.objects.create(
                phone_number=data.get('phone_number'),
                email=data.get('email'),
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                password=data.get('password'),
                is_active=True
            )
            user.save()
            front_image = PassportFront.objects.create(
                user=user,
                front_image=data.get('front_image')
            )
            front_image.save()
            back_image = PassportBack.objects.create(
                user=user,
                back_image=data.get('back_image')
            )
            back_image.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        return ProfileSerializer

    def get_queryset(self):
        return User.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)
