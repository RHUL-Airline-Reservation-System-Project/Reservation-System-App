from rest_framework import serializers
from .models import CheckIn

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = "__all__"



#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
