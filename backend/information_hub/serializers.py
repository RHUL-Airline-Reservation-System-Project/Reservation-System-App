from rest_framework import serializers
from .models import InformationHub

class InformationHubSerializer(serializers.ModelSerializer):
    #serializers are responsible of turning various datatypes into native Python datatypes that can be rendered into JSON and vice verse
    class Meta:
        model = InformationHub
        fields = "__all__"



#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer