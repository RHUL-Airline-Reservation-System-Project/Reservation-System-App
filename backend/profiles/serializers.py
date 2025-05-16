from rest_framework import serializers
from .models import Profiles, TierBenefit

#serializers are responsible of turning various datatypes into native Python datatypes that can be rendered into JSON and vice verse

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
