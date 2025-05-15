from rest_framework import serializers
from .models import FlightTracker, Seat

class FlightTrackerSerializer(serializers.ModelSerializer):
    seats_remaining = serializers.SerializerMethodField()
    class Meta:
        model = FlightTracker
        fields = [ "id","flight_number", 
                  "flight_status",
                  "departure_time", 
                  "arrival_time", 
                  "departure_location",
                  "destination",
                  "seats_remaining"]

    def get_seats_remaining(self, obj):
        return obj.seats.filter(available=True).count()
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
#https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
#https://docs.djangoproject.com/en/5.2/ref/models/meta/#field-objects
#https://docs.djangoproject.com/en/5.2/topics/db/queries/#retrieving-specific-objects-with-filters
