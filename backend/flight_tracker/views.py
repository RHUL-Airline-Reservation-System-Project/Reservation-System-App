from rest_framework import viewsets
from .models import FlightTracker
from .serializers import FlightTrackerSerializer

class FlightTrackerView(viewsets.ModelViewSet):
    queryset = FlightTracker.objects.all()
    serializer_class = FlightTrackerSerializer
    


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/
