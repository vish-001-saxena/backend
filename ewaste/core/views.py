from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PickupRequest
from .serializers import PickupRequestSerializer
from .forms import RegistrationForm, PickupForm

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def create_pickup(request):
    serializer = PickupRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

def registration_page(request):
    return render(request, 'registration.html')
def tracking (request):
    return render(request, 'tracking.html')
def blog (request):
    return render(request,'blog.html')
def category(request):
    return render(request, 'category.html')

def app(request):
    return render(request, 'app.html')


# views.py
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def registration_success(request):
    return render(request, 'success.html')


def Pickup_order(request):
    if request.method == "POST":
        form = PickupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = PickupForm()

    return render(request, 'pickup.html', {'form': form})

