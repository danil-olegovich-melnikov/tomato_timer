from django.urls import path

from . import views

app_name = 'circles'

urlpatterns = [
    path("", views.main, name="main")
]