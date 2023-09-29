from django.shortcuts import render
from django.contrib.auth.views import LoginView


class Home(LoginView):
    fields = '__all__'
    template_name = 'home.html'
