from django.core.management.base import BaseCommand
from rooms.models import Amenity


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
        amenities = [
                "Kitchen",
                "Shampoo",
                "Heating",
                "Air conditioning",
                "Washer",
                "Dryer",
                "Wifi",
                "Breakfast",
                "Indoor fireplace",
                "Hangers",
                "Iron",
                "Hair dryer",
                "Dedicated workspace",
                "TV",
                "Crib",
                "High chair",
                "Self check-in",
                "Smoke alarm",
                "Carbon monoxide alarm",
                "Private bathroom",
                "Piano",
        ]
        
        for a in amenities:
            Amenity.objects.create(name = a)
    
        self.stdout.write(self.style.SUCCESS( "Amenities created!!" ) ) 
    
        
