from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'handler'

urlpatterns = [
    path("", views.main, name="main"),
]