from django.urls import path

from apps.tracking import views

urlpatterns = [
    path('track-code/', views.TrackCodeAPI.as_view(), name='track-code'),
]
