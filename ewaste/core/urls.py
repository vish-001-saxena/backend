from django.urls import path
from . import views
from .views import create_pickup

urlpatterns = [
    path('', views.home, name='home'),
    path('api/pickup/', create_pickup),
]
