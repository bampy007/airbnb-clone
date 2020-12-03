from django.core.management.base import BaseCommand

from django_seed import Seed

from users.models import User



class Command(BaseCommand):
    print("# command action #")
    
    help = "This command creates many users"
    
    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="How many users do you want to create?")

    def handle(self, *args, **options):
        number = options.get("number")
        
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "superhost": False})
        seeder.execute()
            
      #  for a in amenities:
      #      Amenity.objects.create(name = a)
    
        self.stdout.write(self.style.SUCCESS( f"{number} Users created!!" ) ) 
    
        