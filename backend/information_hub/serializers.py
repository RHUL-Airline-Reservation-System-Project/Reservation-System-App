from rest_framework import serializers
from .models import InformationHub

class InformationHubSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationHub
        fields = "__all__"



#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer