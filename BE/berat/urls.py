from django.urls import path
from .views import * 

urlpatterns = [
    path('', berat_form, name='berat_form'),
    path('list', berat_list, name='berat_list'),
    path('<int:id>/', berat_form, name="update_berat"),
    path('delete/<int:id>/', berat_delete, name="delete_berat"),
]
