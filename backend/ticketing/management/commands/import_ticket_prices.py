from django.core.management.base import BaseCommand
from backend.flight_tracker.models import FlightTracker
from backend.ticketing.models import Ticketing
#base commands are used by management and manage.py they are at the root of each file if created
class Command(BaseCommand):
    help = "Create ticket prices for each flight and class"

    def handle(self, *args, **opts):
        #tier prices for different class types
        tiers = {
            "ECONOMY": 50.00,
            "ECONOMY_PLUS": 80.00,
            "BUSINESS": 200.00,
            "FIRST": 400.00
        }
        #assigns said prices for the seat types
        for flight in FlightTracker.objects.all():
            for cls, price in tiers.items():
                Ticketing.objects.update_or_create(
                    flight_number = flight.flight_number,
                    class_type = cls,
                    defaults={"price": price, "discount_code": "", "is_available": "yes"}
                )
        self.stdout.write(self.style.SUCCESS("Ticket prices implemented."))
        #alert for successful assignment
#https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/
#https://docs.djangoproject.com/en/5.2/ref/models/querysets/#update-or-creat
