from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('vehicles/add/', views.AddVehicle.as_view(), name='add_vehicle'),
    path('vehicles/', views.vehicle_index, name='vehicle_index'),
    path('vehicles/<int:pk>/', views.VehicleDetail.as_view(), name='vehicle_detail'),
    path('vehicles/<int:pk>/update/',
         views.VehicleUpdate.as_view(), name='vehicle_update'),
    path('vehicles/<int:pk>/sell/', views.SellVehicle.as_view(), name='sell_vehicle'),
    path('vehicles/<int:pk>/delete/',
         views.VehicleDelete.as_view(), name='vehicle_delete'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('locations/add', views.AddLocation.as_view(), name='add_location'),
]
