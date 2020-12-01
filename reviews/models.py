from django.db import models

from core import models as core_models
from users import models as user_models
from rooms import models as room_models

# Create your models here.

class Review(core_models.TimeStampedModel):
    
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness= models.IntegerField()
    location= models.IntegerField()
    check_in= models.IntegerField()
    value = models.IntegerField()
    
    user = models.ForeignKey(user_models.User, related_name="reviews", on_delete=models.CASCADE)  
    room = models.ForeignKey(room_models.Room, related_name="reviews", on_delete=models.CASCADE)
    
    """ Upgrade! """
    def __str__(self):
        return f"{self.review} - {self.room.name}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
            ) / 6
        return avg 
    