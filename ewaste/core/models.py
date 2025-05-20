from django.db import models

# Create your models here.


class PickupRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    device_type = models.CharField(max_length=50)
    scheduled_date = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.device_type}"


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone= models.CharField(max_length=15)
    
    

    def __str__(self):
        return self.name

