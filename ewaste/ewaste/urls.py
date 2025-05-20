from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Replace with your app's name
    path('', views.home, name='home'),  
    path('api/pickup/', views.create_pickup),  # already there
    path('registration.html', views.registration_page, name='registration'),
    path('pickup.html', views.Pickup_order, name='pickup'),
    path('tracking.html', views.tracking, name='tracking'),
    path('category.html', views.category, name='category'),
    path('blog.html', views.blog , name='blog'),
    path('app.html', views.app , name='app')
]
