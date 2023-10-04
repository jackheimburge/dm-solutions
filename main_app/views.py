from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, ListView
from .models import Vehicle, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin


class Home(LoginView):
    fields = '__all__'
    template_name = 'home.html'


class AddVehicle(PermissionRequiredMixin, CreateView):
    permission_required = 'add_vehicle'
    model = Vehicle
    fields = ['year', 'make', 'model', 'msrp', 'color', 'notes', 'engine', 'odometer', 'interior', 'transmission' , 'condition',
    'vehicle_type', 'location', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Vehicle'
        return context

def vehicle_index(request):
    vehicles = Vehicle.objects.all()

    return render(request, 'vehicles/index.html', {
        'vehicles': vehicles,
        'title': 'Vehicle List'
    })


class VehicleDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'view_vehicle'
    model = Vehicle


class VehicleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'change_vehicle'
    model = Vehicle
    fields = ['notes', 'condition', 'odometer', 'is_available', 'image']


class VehicleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_vehicle'
    model = Vehicle
    success_url = '/vehicles'

class Dashboard(ListView):
    model = Vehicle

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user).order_by('-sold_for')

class AddLocation(CreateView):
    model = Location
    fields = '__all__'
