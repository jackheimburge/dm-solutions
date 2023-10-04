from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, ListView
from .models import Vehicle, Location
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse


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


class SellVehicle(PermissionRequiredMixin, UpdateView):
    permission_required = 'change_vehicle'
    model = Vehicle
    fields = ['sold_for', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_available = False
        return super().form_valid(form)



class VehicleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_vehicle'
    model = Vehicle
    success_url = '/vehicles'

class Dashboard(ListView):
    model = Vehicle

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user).order_by('-sold_for')


class AddLocation(PermissionRequiredMixin, CreateView):
    permission_required = 'add_location'
    model = Location
    fields = '__all__'

def total_sales(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    labels = [x + 1 for x in range(len(vehicles))]
    data = []
    for index, obj in vehicles:
        if index == 0:
            data.append(obj.sold_for)
        else:
            data.append(obj.sold_for + data.at(index - 1))

    return JsonResponse({
        'title': 'Total Sales',
        'data': {
            'labels': labels,
            'datasets': [{
                'label': 'Sale Amount',
                'data': data,
            }]
        }

    })
