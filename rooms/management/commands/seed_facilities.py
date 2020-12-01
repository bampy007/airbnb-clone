from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    print("# command action #")
    
    help = "This command tells me that he loves me"
   
    def handle(self, *args, **options):
        facilities = [
                "Laundry01",
                "GYM01",
                "Parking01",
                "Elevator01",
                "Laundry02",
                "GYM02",
                "Parking02",
                "Elevator02",
                "Laundry03",
                "GYM03",
                "Parking03",
                "Elevator03",
                "Laundry04",
                "GYM04",
                "Parking04",
                "Elevator04",
        ]
        
        for a in facilities:
            Facility.objects.create(name = a)


        targetType = "Facilities"    
        self.stdout.write(self.style.SUCCESS( f"{targetType} created!!" ) ) 
        
        
