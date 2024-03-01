from django.db import models
from django.utils import timezone
import datetime

class mobiles(models.Model):
    name=models.CharField(max_length=100)
    des=models.CharField(max_length=100)
    img = models.ImageField(upload_to ='uploads/') 
    date=models.DateField()
    

