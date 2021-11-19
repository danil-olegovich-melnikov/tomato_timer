from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'handler'

urlpatterns = [
    path("profile/", views.main, name="main"),
    path("", TemplateView.as_view(template_name="timer_tasks/index.html"), name="home")
]