from django.urls import path
from . import views

urlpatterns = [
    path('flowers/', views.flower_list, name='flower_list'),
    path('bouquets/', views.bouquet_list, name='bouquet_list'),
]
