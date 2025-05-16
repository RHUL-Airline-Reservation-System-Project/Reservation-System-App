from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer
#views are callables that take a request and return a response
#viewsets have basic crud commands, making it easier to use
class MenuItemView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/


