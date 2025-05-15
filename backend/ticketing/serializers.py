from rest_framework import serializers
from .models import Ticketing

class TicketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticketing
        fields = "__all__"

#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
