from django.urls import path, include
from .views import identify_customer

urlpatterns = [
    path('identify', identify_customer),
]