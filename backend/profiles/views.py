from rest_framework import viewsets
from .models import Profiles, TierBenefit
from .serializers import ProfilesSerializer, TierBenefitSerializer


#views are callables that take a request and return a response
#viewsets have basic crud commands, making it easier to use
class ProfilesView(viewsets.ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer

class BenefitView(viewsets.ModelViewSet):
    queryset = TierBenefit.objects.all()
    serializer_class = TierBenefitSerializer


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/