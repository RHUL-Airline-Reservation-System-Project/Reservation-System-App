from rest_framework import viewsets
from .models import FlightTracker, Seat
from .serializers import FlightTrackerSerializer, SeatSerializer

class FlightTrackerView(viewsets.ModelViewSet):
    queryset = FlightTracker.objects.all()
    serializer_class = FlightTrackerSerializer

class SeatView(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/
