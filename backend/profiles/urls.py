from django.urls import path, include
from .views import ProfilesView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiles", ProfilesView)

urlpatterns = [
    path("", include(router.urls)),
]

#https://www.django-rest-framework.org/api-guide/routers/
#https://docs.djangoproject.com/en/5.2/topics/http/urls/