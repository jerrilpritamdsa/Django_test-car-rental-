from django.urls import path
from .views import VehicleDetailView
urlpatterns = [
    path('',VehicleDetailView.as_view())
]