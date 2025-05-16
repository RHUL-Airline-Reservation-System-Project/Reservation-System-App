from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from backend.flight_tracker.models import Seat
from .models import CheckIn
from .serializers import CheckInSerializer

#views are callables that take a request and return a response
#viewsets have basic crud commands, making it easier to use
class CheckInView(viewsets.ModelViewSet):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer


    @action(detail=False, methods=["get"], url_path="seats")
    def seats(self, request):
        flight_num = request.query_params.get("flight")
        seats = Seat.objects.filter(flight__flight_number=flight_num)
        data = [{"row": Seat.row, "letter": Seat.letter, "class":Seat.seat_class, "available": Seat.available}
                for s in seats]
        return Response(data)
    #uses data from Seat model and assigns it when a user tries to check in to a specific seat, looks for class and availability also



#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/