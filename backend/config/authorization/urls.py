import django.contrib.auth.views as auth_views
from django.urls import path

from . import views

app_name = 'authorization'
urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='authorization/login.html', ), name='login'),
]
