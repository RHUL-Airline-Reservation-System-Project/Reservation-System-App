from rest_framework import serializers
from .models import Profiles, TierBenefit

class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = "__all__"

class TierBenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TierBenefit
        fields = "__all__"


#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
