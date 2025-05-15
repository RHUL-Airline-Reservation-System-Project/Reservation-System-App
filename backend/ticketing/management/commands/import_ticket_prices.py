from django.core.management.base import BaseCommand
from backend.flight_tracker.models import FlightTracker
from backend.ticketing.models import Ticketing

class Command(BaseCommand):
    help = "Create ticket prices for each flight and class"

    def handle(self, *args, **opts):
        tiers = {
            "Economy": 50.00,
            "Economy Plus": 80.00,
            "Business": 200.00,
            "First": 400.00
        }

        for flight in FlightTracker.objects.all():
            for cls, price in tiers.items():
                Ticketing.objects.update_or_create(
                    flight_number = flight.flight_number,
                    class_type = cls,
                    defaults={"price": price, "discount_code": "", "is_available": "yes"}#TODO: Add discount codes, make the is_availabe changeable
                )
        self.stdout.write(self.style.SUCCESS("Ticket prices implemented."))

#https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/
#https://docs.djangoproject.com/en/5.2/ref/models/querysets/#update-or-create

            