from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import Profiles, TierBenefit
from .serializers import ProfilesSerializer, TierBenefitSerializer
import math


class ProfilesView(viewsets.ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer

class BenefitView(viewsets.ModelViewSet):
    queryset = TierBenefit.objects.all()
    serializer_class = TierBenefitSerializer


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/