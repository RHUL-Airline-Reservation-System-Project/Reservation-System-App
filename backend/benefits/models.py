from django.db import models

class Benefits(models.Model):
    benefit = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    miles_needed = models.IntegerField()
    discount_rate = models.DecimalField(max_digits=6,decimal_places=4)

    def __str__(self):
        return self.benefit


#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
