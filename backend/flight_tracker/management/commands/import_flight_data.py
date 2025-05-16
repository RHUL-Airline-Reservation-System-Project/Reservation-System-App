import csv 
from django.core.management.base import BaseCommand
from backend.flight_tracker.models  import FlightTracker  
from backend.information_hub.models import InformationHub
#base commands are used by management and manage.py they are at the root of each file if created

class Command(BaseCommand):
    help = "Loads chatgpt generated dataset into FlightTracker and InformationHub"

    def handle(self, *args, **opts):
        objs = []
        with open("real_flights_dataset.csv") as fd:
            reader = csv.DictReader(fd)
            for row in reader:
                
                objs.append(FlightTracker(
                    flight_number = row["flight_number"],
                    flight_status = row["status"],
                    departure_time = row["scheduled_departure"],
                    arrival_time = row["scheduled_arrival"],
                    departure_location = row["origin"],
                    destination = row["destination"]
                ))
                #reads csv file and assigns it to flight tracker models for storing and grabbing data
                
                

                InformationHub.objects.update_or_create(
                flight_number = row["flight_number"],
                defaults = {
                    "status_update": row["status"],
                    "gate_number": row["departure_gate"],
                    "cancellation": "Yes" if row["cancelled"] == "True" else "No",
                    "delay": row["delay_minutes"] or "0"
                    }
                ) 
                #uses the alread read csv file for information hub models that need data 
        FlightTracker.objects.bulk_create(objs, ignore_conflicts=True) 
        self.stdout.write(self.style.SUCCESS("Imported all flights & gate info."))
        #alert for successful importation
        

#https://www.geeksforgeeks.org/reading-csv-files-in-python/
#https://docs.djangoproject.com/en/5.2/howto/custom-management-commands/
#https://docs.djangoproject.com/en/5.2/ref/models/querysets/#update-or-create
#https://docs.djangoproject.com/en/5.2/ref/models/querysets/#bulk-create

