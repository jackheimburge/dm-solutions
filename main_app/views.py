from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, ListView
from .models import Vehicle, Location
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm


class Home(LoginView):
    fields = '__all__'
    template_name = 'home.html'


def signup(request):
    error_message = ''
    employee_group, created = Group.objects.get_or_create(name="Employee")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(employee_group)
            login(request, user)
            return redirect('/dashboard')
        else:
            error_message = "Invalid sign up. Please try again...please."
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message, 'title': 'Sign Up'}
    return render(request, 'registration/signup.html', context)


class AddVehicle(PermissionRequiredMixin, CreateView):
    permission_required = 'add_vehicle'
    model = Vehicle
    fields = ['year', 'make', 'model', 'msrp', 'color', 'notes', 'engine', 'odometer', 'interior', 'transmission', 'condition',
              'vehicle_type', 'location', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Vehicle'
        return context

@login_required
def vehicle_index(request):
    sort = request.GET.get('sort')
    if sort:
        vehicles = Vehicle.objects.order_by(sort)
    else:
        vehicles = Vehicle.objects.all()

    return render(request, 'vehicles/index.html', {
        'vehicles': vehicles,
        'title': 'Vehicle List'
    })


class VehicleDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'main_app.view_vehicle'
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Vehicle Detail'
        return context


class VehicleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'main_app.change_vehicle'
    model = Vehicle
    fields = ['notes', 'condition', 'odometer', 'image']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Vehicle Update'
        return context


class SellVehicle(PermissionRequiredMixin, UpdateView):
    permission_required = 'main_app.change_vehicle'
    model = Vehicle
    fields = ['sold_for', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.is_available = False
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sell Vehicle'
        return context


class VehicleDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'main_app.delete_vehicle'
    model = Vehicle
    success_url = '/vehicles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Vehicle Delete'
        return context


class Dashboard(LoginRequiredMixin, ListView):
    model = Vehicle

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"{self.request.user.username}'s Dashboard"
        return context

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user).order_by('-sold_for')


class AddLocation(PermissionRequiredMixin, CreateView):
    permission_required = 'main_app.add_location'
    model = Location
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Location'
        return context


def total_sales(request):
    vehicles = Vehicle.objects.filter(user=request.user)
    labels = []
    data = []
    total_sales_amount = 0

    for index, obj in enumerate(vehicles):
        labels.append(index + 1)
        total_sales_amount += obj.sold_for
        data.append(total_sales_amount)

    return JsonResponse({
        'title': 'Total Sales',
        'data': {
            'labels': labels,
            'datasets': [{
                'label': 'Total Sold($)',
                'data': data,
                'backgroundColor': 'Grey',
                'borderColor': 'Black',
                'pointStyle': 'circle'
            }]
        }

    })


def sales_by_make(request):
    vehicles = Vehicle.objects.filter(user=request.user)

    labels = []
    data = []
    occurences = {}

    for vehicle in vehicles:
        make = vehicle.make
        if make in occurences:
            occurences[make] += 1
        else:
            occurences[make] = 1

    for make, occ in occurences.items():
        labels.append(make)
        data.append(occ)

    return JsonResponse({
        'title': 'Sales By Make',
        'data': {
            'labels': labels,
            'datasets': [{
                'label': 'Sold',
                'data': data,
                'backgroundColor': ['Pink', 'Purple', 'Orange', 'Yellow'],
                'borderColor': 'Black',
            }]
        }

    })
