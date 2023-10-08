from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm
# Create your views here.


def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    return render(request, 'app_auth/login.html')


def register_view(request):
    return render(request, 'app_auth/register.html')


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('main-page')
    template_name = 'app_auth/register.html'
