from django.core.management.base import BaseCommand
from backend.flight_tracker.models import FlightTracker, Seat

class Command(BaseCommand):
    help= "Generate seats for a 200 capacity plane per flight with accurate classes"

    def handle(self, *args, **opts):
        for f in FlightTracker.objects.all():
            seats = []

            for r in (1,2):
                for L in ("A","B","E","F"):
                    seats.append(Seat(flight=f, row=r, letter=L, seat_class="FIRST"))
            for r in (3,4,5):
                for L in ("A","B","E","F"):
                    seats.append(Seat(flight=f, row=r, letter=L, seat_class="BUSINESS"))
            for r in range(6,16):
                for L in ("A","B","C","D","E","F"):
                    seats.append(Seat(flight=f, row=r, letter=L, seat_class="ECONOMY_PLUS"))
            for r in range(16,36):
                for L in ("A","B","C","D","E","F"):
                    seats.append(Seat(flight=f, row=r, letter=L, seat_class="ECONOMY")) 
            Seat.objects.bulk_create(seats, ignore_conflicts=True)
        self.stdout.write(self.style.SUCCESS("200 seats generated for each flight"))