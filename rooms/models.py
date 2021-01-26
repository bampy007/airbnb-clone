from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField

from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):
    
    """ Abstract Item """
    name = models.CharField(max_length = 80)
    #subtitle = models.CharField(max_length = 80)
    #memo = models.CharField(max_length = 80)
      
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name
   
    def newMethod():
        return "potato"


    
class RoomType(AbstractItem):
    """ RoomType Model Definition """
    
    class Meta:
        verbose_name = "Room Types"
        ordering = ['-name']
    pass
    
class Amenity(AbstractItem):
    """ Amenity  Model Definition """
    class Meta:
            verbose_name_plural = "Amenities"
    pass
    
class Facility(AbstractItem):
    """ Facility  Model Definition """
    class Meta:
            verbose_name_plural = "Facilities"
    pass
        
class HouseRule(AbstractItem):
    """ HouseRule  Model Definition """
    class Meta:
             verbose_name = "House Rule"
    pass
    
    
class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition """
    
    caption = models.CharField(max_length = 40)
    file = models.ImageField(upload_to = "room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE) #"Room : class name"
    
    def __str__(self):
        return self.caption
    
    pass
    
    

class Room(core_models.TimeStampedModel):
    
    """ Room Model Definition """
    #Use Django_counties
    
    name = models.CharField(max_length = 140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length = 40)
    price = models.IntegerField()
    address = models.CharField(max_length = 40)
    
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default = False)
    
    #relationShip : many to one, many to many
    host = models.ForeignKey(user_models.User, related_name="rooms", on_delete=models.CASCADE) 
    room_type = models.ForeignKey(RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True)
       
    #
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms",)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)
    
    
    """ Upgrade! """
    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        print(self.city)
        self.city = str.capitalize(self.city)
        print(self.city)
        super().save(*arg, **kwargs)   #call the real save() method
        print("room- saved")
    
    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
    

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        
        count = len(all_reviews)
        if count > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            
            avg_rating = all_ratings / count
            return round(avg_rating)
        return 0

 #       ret_total_rating = 0
 #       if (len(all_reviews) =! 0) :
 #           ret_total_rating = all_ratings / len(all_reviews) 
 #       else:
 #           ret_total_rating = 0
            

            