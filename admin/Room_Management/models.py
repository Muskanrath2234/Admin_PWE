from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=50)
    available_seat = models.IntegerField()
    TYPE_CHOICES = [
        ('single', 'Single'),
        ('double', 'Double'),
        ('triple', 'Triple'),
        ('customized', 'Customized'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    available_date = models.DateField(null=True,blank=True)
    floor = models.IntegerField()

    def __str__(self):
        return self.room_number

# models.py
from django.db import models

class Facility(models.Model):
    FACILITY_TYPES = [
        ('gym', 'Gym'),
        ('pool', 'Swimming Pool'),
        ('wifi', 'WiFi'),
        ('laundry', 'Laundry'),
        ('parking', 'Parking'),
        ('other', 'Other'),
    ]

    facility_type = models.CharField(max_length=20, choices=FACILITY_TYPES,blank=True, null=True)
    facility_name = models.CharField(max_length=100,blank=True, null=True)
    facility_image = models.ImageField(upload_to='facility_images/', blank=True, null=True)

    def __str__(self):
        return self.facility_name


