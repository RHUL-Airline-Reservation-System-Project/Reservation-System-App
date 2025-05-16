from django.db import models

class InformationHub(models.Model):
    #models contain information about data and contain parameters and behaviours
    #these models contaion basic information you would see at an airport terminal or in this case,
    #the airline reservation system
    flight_number = models.CharField(max_length = 100)
    status_update = models.CharField(max_length = 100)
    gate_number = models.CharField(max_length = 100)
    cancellation = models.CharField(max_length = 100)
    delay = models.CharField(max_length = 100)

    def __str__(self):
        return self.flight_number
    
#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
