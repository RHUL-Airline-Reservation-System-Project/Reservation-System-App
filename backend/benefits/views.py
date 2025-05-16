from rest_framework import viewsets
from .models import Benefits
from .serializers import BenefitSerializer
#views are callables that take a request and return a response
#viewsets have basic crud commands, making it easier to use
class BenefitView(viewsets.ModelViewSet):
    queryset = Benefits.objects.all()
    serializer_class = BenefitSerializer
    #uses its own serializer and model for

#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/