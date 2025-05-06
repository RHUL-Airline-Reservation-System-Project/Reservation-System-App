from django.db import models

class Benefits(models.Model):
    benefit = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    miles_needed = models.CharField(max_length=100)
    discount_rate = models.CharField(max_length=100)

    def __str__(self):
        return self.benefit


#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
