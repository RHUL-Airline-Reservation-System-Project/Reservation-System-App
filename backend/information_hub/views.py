from rest_framework import viewsets
from rest_framework.response import Response
from .models import InformationHub
from .serializers import InformationHubSerializer
from backend.check_in.models import CheckIn
from backend.check_in.serializers import CheckInSerializer
from backend.benefits.models import Benefits
from backend.benefits.serializers import BenefitSerializer
from backend.flight_tracker.models import FlightTracker
from backend.flight_tracker.serializers import FlightTrackerSerializer


class InformationHubView(viewsets.ModelViewSet):
    queryset = InformationHub.objects.all()
    serializer_class = InformationHubSerializer

    def list(self, request, *args, **kwargs):
        information_data = super().list(request, *args, **kwargs).data

        checkin = CheckInSerializer(CheckIn.objects.all(), many=True).data
        benefit = BenefitSerializer(Benefits.objects.all(), many=True).data
        tracking = FlightTrackerSerializer(FlightTracker.objects.all(), many=True).data

        return Response({
            "info_hub": information_data,
            "check_ins": checkin,
            "benefits": benefit,
            "tracking": tracking,
        })


#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets
#https://www.django-rest-framework.org/api-guide/viewsets