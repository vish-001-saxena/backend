from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PickupRequest
from .serializers import PickupRequestSerializer

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
def pickup(request):
    return render(request, 'pickup.html')
def app(request):
    return render(request, 'app.html')