from rest_framework import viewsets
from .models import Benefits
from .serializers import BenefitSerializer

class BenefitView(viewsets.ModelViewSet):
    queryset = Benefits.objects.all()
    serializer_class = BenefitSerializer


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/