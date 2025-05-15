from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
import random
from .models import Ticketing, Booking, Payment
from backend.flight_tracker.models import Seat
from .serializers import TicketingSerializer, BookingSerializer, PaymentSerializer
import uuid



class TicketingView(viewsets.ModelViewSet):
    queryset = Ticketing.objects.all()
    serializer_class = TicketingSerializer
class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    

    def perform_create(self, serializer):
        seat_str = serializer.validated_data.get("seat")
        flight = serializer.validated_data["flight"]
        row, letter = int(seat_str[:-1]), seat_str[-1]


        try:
            seat_obj = Seat.objects.get(flight=flight, 
                                        row=int(seat_str[:-1]), 
                                        letter=seat_str[-1], available=True)
        except Seat.DoesNotExist:
            raise ValidationError({"seat": "Unavailable or invalid seat"})
        seat_obj.available = False
        seat_obj.save()

        if row <= 2:
            seat_class ="FIRST"
        elif row <=5:
            seat_class = "BUSINESS"
        elif row <=15:
            seat_class = "ECONOMY_PLUS"
        else:
            seat_class = "ECONOMY"
        
        try:
            ticket = Ticketing.objects.filter(
                flight = flight,
                class_type = seat_class,
                is_available = True).earliest("id")
        except Ticketing.DoesNotExist:
            raise ValidationError({"error":f"No {seat_class} tickets available"})
        ticket.is_available = False
        ticket.save()
        reference = uuid.uuid4().hex[:8].upper()
        serializer.save(booking_reference=reference, ticket=ticket)
    @action(detail=True, methods=["post"])
    def buy(self, request, pk=None):
        booking = self.get_object()

        if not booking.ticket:
            return Response({"error":"No ticket assigned"},status=status.HTTP_400_BAD_REQUEST)
    
        amount = float(booking.ticket.price)

        payment, created = Payment.objects.get_or_create(booking=booking, defaults={"amount":amount, "status":"PENDING"})

        if not created:
            if payment.status == "PAID":
                return Response({"error":"Bokking already paid"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not created and payment.status in {"FAILED","REFUNDED"}:
            payment.status = "PENDING"
            payment.amount = amount
            payment.save()
        
        r = random.random()
        if r < 0.9:
            payment.status = "PAID"
            booking.status = "CONFIRMED"
            outcome = {"status": "paid"}
            response_status=status.HTTP_200_OK
        elif r < 0.93:
            payment.status ="FAILED"
            booking.status = "PENDING"

            row, letter = int(booking.seat[:-1]), booking.seat[-1]
            seat = Seat.objects.get(flight=booking.flight, row=row, letter=letter)
            seat.available=True
            seat.save()
            outcome = {"status":"failed"}
            response_status= status.HTTP_402_PAYMENT_REQUIRED
        else:
            payment.status = "REFUNDED"
            booking.status = "CANCELLED"
            row, letter = int(booking.seat[:-1]), booking.seat[-1]
            seat = Seat.objects.get(flight=booking.flight, row=row, letter=letter)
            seat.available=True
            seat.save()
            outcome = {"status":"refunded"}
            response_status = status.HTTP_200_OK
        
        payment.save()
        booking.save()

        return Response({**outcome, "amount":amount}, status=response_status)
        
class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    

#https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#https://docs.djangoproject.com/en/stable/ref/models/querysets/
#https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
#https://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
#https://www.django-rest-framework.org/api-guide/generic-views/#perform_create
#https://www.django-rest-framework.org/api-guide/exceptions/#validationerror

