from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
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
    path('api/total_sales/', views.total_sales, name='total_sales'),
    path('api/sales_by_make/', views.sales_by_make, name='sales_by_make'),
]
