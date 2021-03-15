from django.urls import path
from .views import factoryView, factoryDetailView, dealershipDetailView, dealershipView, indexView

urlpatterns = [
    path('factory/', factoryView, name='factory_url'),
    path('factory/<int:factory_id>/', factoryDetailView, name='detailed_factory_url'),
    path('dealership/', dealershipView, name='dealership_url'),
    path('dealership/<int:dealership_id>/', dealershipDetailView, name='detailed_dealership_url'),
    path('', indexView, name='index'),
]
