from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, ListView
from .models import Vehicle, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class Home(LoginView):
    fields = '__all__'
    template_name = 'home.html'


class AddVehicle(CreateView):
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

class VehicleDetail(DetailView):
    model = Vehicle

class VehicleUpdate(UpdateView):
    model = Vehicle
    fields = ['notes', 'condition', 'odometer', 'is_available', 'image']


class VehicleDelete(DeleteView):
    model = Vehicle
    success_url = '/vehicles'

class Dashboard(ListView):
    model = Vehicle

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user).order_by('-sold_for')

class AddLocation(CreateView):
    model = Location
    fields = '__all__'
