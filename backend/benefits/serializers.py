from rest_framework import serializers
from .models import Benefits

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = "__all__"



#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer