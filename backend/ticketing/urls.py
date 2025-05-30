from django.urls import path, include
from .views import TicketingView, BookingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"ticketing", TicketingView)
router.register(r"bookings", BookingView)
#routers help with declaring common routes for view logic with automatic paths(Defaultrouter)
urlpatterns = [
    path("", include(router.urls))
]

#https://www.django-rest-framework.org/api-guide/routers/
#https://docs.djangoproject.com/en/5.2/topics/http/urls/

