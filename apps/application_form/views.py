from rest_framework.views import APIView
from rest_framework.response import Response
from apps.shared.mails.mail_helpers import send_mail
from .serializers import ContactFormSerializer


class ContactFormView(APIView):
    serializer_class = ContactFormSerializer

    def post(self, request, *args, **kwargs):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            telegram = serializer.validated_data.get('telegram', '')
            phone_number = serializer.validated_data.get('phone_number', '')
            recipient_list =['mirbekm352@gmail.com']
            send_mail(
                f"Новое сообщение от {name}",
                f"""Email: {email}\nTelegram: {telegram}\nPhone: {phone_number}\n\n{message}""",
                recipient_list=recipient_list,
            )

            return Response({'message': 'Письмо успешно отправлено!'})
        else:
            return Response(serializer.errors, status=400)
