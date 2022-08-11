from django.db import models
import uuid

# Create your models here.
class Event(models.Model):
    owner_first_name = models.CharField(blank=True, null=True, max_length=150)
    owner_last_name = models.CharField(blank=True, null=True, max_length=150)
    name = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(blank=True, null=True)
    date = models.DateField()
    hall = models.CharField(blank=True, null=True, max_length=200)
    status = models.CharField(null=True, blank=True, default='Pending', max_length=20)
    id = models.CharField(max_length=5, primary_key=True, unique=True)
    
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    fname = models.CharField(blank=True, null=True, max_length=150)
    lname = models.CharField(blank=True, null=True, max_length=150)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(blank=True, null=True, max_length=150)
    message = models.CharField(blank=True, null=True, max_length=3000)

    def __str__(self):
        return self.fname

