from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"



#https://www.django-rest-framework.org/api-guide/serializers/
#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
