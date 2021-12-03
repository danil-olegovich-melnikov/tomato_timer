from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms


# Create your views here.
class UserSignUpView(CreateView):
    form_class = forms.UserSignUpForm
    success_url = "/"
    template_name = 'authorization/signup.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)