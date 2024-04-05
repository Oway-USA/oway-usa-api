import time

import requests
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.tracking.serializers import TrackCodeSerializer
from rest_framework.views import APIView
from oway_usa_api.settings import API_KEY_TRACK

import logging
import requests
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from lxml import html


class TrackCodeAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = TrackCodeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            tracking_number = serializer.validated_data['tracking_number']
            track_response = self.track_package(tracking_number)
            if track_response:
                return Response(track_response, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Невозможно отследить посылку с данным трек-кодом."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def track_package(self, tracking_number):
        POST_URL = "http://info.russianpost.ru/servlet/post_item?action=search&searchType=barCode&show_form=no&barCode={}&page=1".format(
            tracking_number)

        try:
            response = requests.get(POST_URL)
            response.raise_for_status()
            page = html.fromstring(response.content)
            status = page.xpath('//table/tr/td/text()')
            if status:
                return {"status": status}
            else:
                return None
        except requests.RequestException as e:
            return None

