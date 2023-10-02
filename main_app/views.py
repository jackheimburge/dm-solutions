from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .models import Vehicle, Location
from django.views.generic.edit import CreateView


class Home(LoginView):
    fields = '__all__'
    template_name = 'home.html'


class AddVehicle(CreateView):
    model = Vehicle
    fields = ['year', 'make', 'model', 'msrp', 'color', 'notes', 'engine', 'odometer', 'interior', 'transmission' , 'condition',
    'vehicle_type', 'location']
