from django.urls import path
from .views import * 

urlpatterns = [
    path('', berat_form, name='berat_form'),
    path('list', berat_list, name='berat_list'),
]
