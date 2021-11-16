from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("handler.urls")),
    path('authorization/', include('authorization.urls')),
]
