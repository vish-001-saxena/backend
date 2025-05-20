from django.urls import path
from .views import create_pickup ,register_user, registration_success

urlpatterns = [
    path('register', register_user, name='register'),
    path('success', registration_success, name='success'),
]
