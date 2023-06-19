
from django.urls import path
from myapp.views import identify_customer

urlpatterns = [
    path('identify', identify_customer),
    path('identify/', identify_customer)
]

