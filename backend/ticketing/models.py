from django.db import models

class Ticketing(models.Model):
    flight_number = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    class_type = models.CharField(max_length=100)
    discount_code = models.CharField(max_length=100)
    is_available = models.CharField(max_length=100)

    def __str__(self):
        return self.flight_number

#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str