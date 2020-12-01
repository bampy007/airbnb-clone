from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    print("# command action #")
    
    help = "This command creates many user"
    
    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, help="How many users do you want me to create?")
       
           
    def handle(self, *args, **options):
        number = options.get("number")

        seeder = Seed.seeder()
        seeder.add_entity(
            User, 
            number, 
            {'is_staff' : False, "is_superuser" : False}
        )
        seeder.execute()

        targetType = "Users" 
        self.stdout.write(self.style.SUCCESS(f"{number} {targetType} created!"))
















    """

    def add_arguments(self, parser):
        parser.add_argument("--times", help="How many times do you want me to tell you?")
       
           
    def handle(self, *args, **options):
        times = options.get("times")
        #print(args, options)
        for t in range(0, int(times)):
            self.stdout.write(self.style.ERROR("I love you") ) 

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
      
      """
        
