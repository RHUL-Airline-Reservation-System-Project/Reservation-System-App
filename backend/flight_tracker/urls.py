from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightTrackerView

router = DefaultRouter()
router.register(r"flight-tracker", FlightTrackerView)

urlpatterns = [
    path("", include(router.urls))
]
#https://www.django-rest-framework.org/api-guide/routers/
#https://docs.djangoproject.com/en/5.2/topics/http/urls/

