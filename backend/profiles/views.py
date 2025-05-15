from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from .models import Profiles
from .serializers import ProfilesSerializer
import math


class ProfilesView(viewsets.ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer




#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/