
from django.urls import path

from .views import *

urlpatterns = [
    path('transfer', index, name="home"),
    path('', home, name="transfer"),
    path('aprove', aprove, name="aprove"),
    path('transfer_list/',transfer_list.as_view(), name='transfer_list'),
    path('transfer_list/<slug:pk>/', transfer_detail.as_view() , name= 'transfer_detail'),
]
