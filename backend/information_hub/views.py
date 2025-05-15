from rest_framework import viewsets
from .models import InformationHub
from .serializers import InformationHubSerlializer

class InformationHubView(viewsets.ModelViewSet):
    queryset = InformationHub.objects.all()
    serializer_class = InformationHubSerlializer


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/