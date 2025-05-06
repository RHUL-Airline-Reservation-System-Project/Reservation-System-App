from rest_framework import viewsets
from .models import Ticketing
from .serializers import TicketingSerializer

class TicketingView(viewsets.ModelViewSet):
    queryset = Ticketing.objects.all()
    serializer_class = TicketingSerializer

#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/
