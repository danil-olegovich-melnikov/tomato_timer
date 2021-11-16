from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms


# Create your views here.
class UserSignUpView(CreateView):
    form_class = forms.UserSignUpForm
    success_url = reverse_lazy('authorization:login')
    template_name = 'authorization/signup.html'
