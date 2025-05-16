from rest_framework import serializers
from .models import Ticketing, Booking, Payment
#serializers are responsible of turning various datatypes into native Python datatypes that can be rendered into JSON and vice verse

class TicketingSerializer(serializers.ModelSerializer):
    booking_reference = serializers.CharField(read_only=True)
    
    class Meta:
        model = Ticketing
        fields = "__all__"
        read_only_fields = ["booking_reference"]
        #booking reference is read only as it is generated 
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__" 
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
