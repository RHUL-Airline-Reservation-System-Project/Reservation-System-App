from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profiles(models.Model):
    #models contain information about data and contain parameters and behaviours
    #user utilizes one to one field so that a username is not replicated, other models are
    #basic profile properties for a functional user profile
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
           on_delete=models.CASCADE, related_name="profile")
    miles_balance = models.IntegerField()
    membership = models.CharField(max_length=100, default="Bronze Tier")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def profile_create_or_update(sender, instance, created, **kwargs):
    if created:
        Profiles.objects.create(user=instance)
    instance.profile.save()
    #creates a user profile that cna be stored
class TierBenefit(models.Model):
    #these models are for different tiers for the membership, tiers are unique and cannot be replicated
    #different discount rates to be applied for each tier, customizable by the frontend,
    #lounge access for specific tiers(boolean)
    tier = models.CharField(max_length=100, unique=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    lounge_access = models.BooleanField(default=False)
    
    
    
#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
#https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#extending-the-existing-user-model
#https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#reusable-apps-and-auth-user-model
#https://docs.djangoproject.com/en/5.2/topics/signals/#django.dispatch.receiver

