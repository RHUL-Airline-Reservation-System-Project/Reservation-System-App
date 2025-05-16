from django.db import models

class FlightTracker(models.Model):
    #models contain information about data and contain parameters and behaviours
    #these are the fields that are connected to the csv file for tracking flights and storing information
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
        
class Seat(models.Model):
    #these models determine basic properties of a seat such as class, row, letter and availability status
    CLASS_CHOICES = [
        ('FIRST',        'First Class'),
        ('BUSINESS',     'Business Class'),
        ('ECONOMY_PLUS', 'Economy Plus'),
        ('ECONOMY',      'Economy'),
    ]

    flight = models.ForeignKey(FlightTracker, on_delete=models.CASCADE, related_name="seats")
    row = models.IntegerField()
    letter = models.CharField(max_length=1)
    seat_class = models.CharField(max_length=20, choices=CLASS_CHOICES)
    available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("flight", "row", "letter")
        #all fields must be true or have a property for this to be a complete model
    
    def __str__(self):
        return f"{self.flight.flight_number} {self.row}{self.letter} ({self.seat_class})"
        
#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
