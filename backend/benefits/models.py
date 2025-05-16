from django.db import models

class Benefits(models.Model):
    #models contain information about data and contain parameters and behaviours
    # defines basic benefit models describing what the benefit is with its description
    # also including the amount of miles needed or if any discounts are applied
    benefit = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    miles_needed = models.IntegerField()
    discount_rate = models.DecimalField(max_digits=6,decimal_places=4, blank=True, null=True)#can be empty field, not essential
    

    def __str__(self):
        return self.benefit


#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
