from django.db import models
from backend.flight_tracker.models import FlightTracker


class Ticketing(models.Model):
    #models contain information about data and contain parameters and behaviours
    #choosing a specific flight, the price dependant on the class type, chooseable class choice,
    #any possible discounts and availability 
    flight = models.ForeignKey(FlightTracker, on_delete=models.CASCADE, related_name="tickets")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    CLASS_CHOICES = [
        ("FIRST", "First Class"),
        ("BUSINESS", "Business Class"),
        ("ECONOMY_PLUS", "Economy Plus"),
        ("ECONOMY", "Economy"),
    ]
    class_type = models.CharField(max_length=20, choices=CLASS_CHOICES)
    discount_code = models.CharField(max_length=100, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.flight_number} - {self.class_type}"
class Booking(models.Model):
    #booking model for importing flights form the csv and assigning passengers,
    #generateable or customizable booking reference, check in and booking confirmation status,
    #and a bookşng time model that automatically gets the time of the booking
    flight = models.ForeignKey(
        "flight_tracker.FlightTracker", 
        on_delete=models.CASCADE, 
        related_name="bookings")
    ticket = models.ForeignKey(Ticketing, on_delete=models.PROTECT, related_name="bookings", null=True, blank=True)
    passenger = models.CharField(max_length=100)
    booking_reference = models.CharField(max_length=8, unique=True, editable=False)
    seat = models.CharField(max_length=4)#this one is now for seat number ratehr than class
    check_in = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[("PENDING","Pending"), ("CONFIRMED", "Confirmed"), ("CANCELLED","Cancelled")], default="PENDING")
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} for {self.passenger}"

class Payment(models.Model):
    #payment model for unique bookings with default pending payment status, amount owed, transaction id
    #and creation time storing model
    booking = models.OneToOneField("Booking", on_delete=models.CASCADE, related_name="payment")
    PAYMENT_STATUS_CHOICES = [
        ("PENDING", "Payment pending"),
        ("PAID", "Payment successful"),
        ("FAILED", "Payment Failed"),
        ("REFUNDED", "Payment refunded")
    ]
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default="PENDING")
    transaction_id = models.CharField(max_length=128, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.status} for booking #{self.booking.id}"
    

#https://docs.djangoproject.com/en/5.2/topics/db/models/
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#charfield
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#integerfield
#https://docs.djangoproject.com/en/5.2/ref/models/instances/#str
#https://docs.djangoproject.com/en/5.1/ref/models/fields/#django.db.models.ForeignKey
#https://docs.djangoproject.com/en/5.2/ref/models/fields/#booleanfield