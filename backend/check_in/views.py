from rest_framework import viewsets
from .models import CheckIn
from .serializers import CheckInSerializer

class CheckInView(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/