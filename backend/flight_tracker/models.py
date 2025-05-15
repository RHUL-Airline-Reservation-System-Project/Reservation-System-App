from django.db import models

class FlightTracker(models.Model):
    flight_number = models.CharField(max_length=100)
    flight_status = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    departure_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

    class Meta:
        ordering = ["departure_time"]
        
        def __str__(self):
           return self.flight_number
    
#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
