from django.db import models

class CheckIn(models.Model):
    #models contain information about data and contain parameters and behaviours
    #generating booking reference, passenger name, seat and extras are essentials for a checkin
    booking_reference = models.CharField(max_length=100)
    passenger_name = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)
    extras = models.CharField(max_length=100)

    def __str__(self):
        return self.booking_reference

#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
