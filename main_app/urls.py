from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('vehicles/add',views.AddVehicle.as_view(), name= 'add_vehicle'),
    path('vehicles/', views.vehicle_index, name='vehicle_index'),
]
