from django.db import models
import uuid

# Create your models here.
def generate_tracking_id():
    return str(uuid.uuid4())[:8].upper()

class PickupRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    device_type = models.CharField(max_length=50)
    scheduled_date = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    tracking_id = models.CharField(max_length=10, unique=True,blank=True,null=True)
    status = models.CharField(max_length=20, default="Pending")


    def __str__(self):
        return f"{self.name} - {self.device_type}"


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone= models.CharField(max_length=15)
    
    
    

    def __str__(self):
        return self.name


