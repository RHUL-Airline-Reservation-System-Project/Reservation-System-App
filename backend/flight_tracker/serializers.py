from rest_framework import serializers
from .models import FlightTracker

class FlightTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightTracker
        fields = "__all__"

#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer