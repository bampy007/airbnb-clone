from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    print("# command action #")
    
    help = "This command tells me that he loves me"
    
    """
    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times do you want me to tell you?")
       
           
    def handle(self, *args, **options):
        times = options.get("times")
        #print(args, options)
        for t in range(0, int(times)):
            self.stdout.write(self.style.ERROR("I love you") ) 
    """     
    
    def handle(self, *args, **options):
        facilities = [
                "Laundry",
                "GYM",
                "Parking",
                "Elevator",
        ]
        
        for a in facilities:
            Facility.objects.create(name = a)
    
        self.stdout.write(self.style.SUCCESS( "Facilities created!!" ) ) 
    
        
