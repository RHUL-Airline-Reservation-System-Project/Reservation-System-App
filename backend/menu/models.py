from django.db import models

class MenuItem(models.Model):
    #models contain information about data and contain parameters and behaviours
    #these models are created for the navbar of the web app, the frontend can assign any name, 
    #icon and url into them
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    icon = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
