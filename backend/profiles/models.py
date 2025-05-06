from django.db import models


class Profiles(models.Model):
    user = models.CharField(max_length=100)
    miles_balance = models.IntegerField()
    membership = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)



    class Meta:
        db_table = "profile-info"
        ordering = ["-createdAt"]

        def __str__(self) -> str:
            return self.user
    
    
    
#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str