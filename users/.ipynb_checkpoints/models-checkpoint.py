from django.contrib.auth.models import AbstractUser
from django.db import models

#doc : model fields
class User(AbstractUser):
    
    """ Custom User Model """
    
    """ CONSTANTS """
    
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    
    GENDER_CHOICES = (
            (GENDER_MALE, "Male"),
            (GENDER_FEMALE, "Female"),
            (GENDER_OTHER, "Other"),
    )
    
    LANG_ENG = "en"
    LANG_KOR = "ko"
    
    LANG_CHOICES = ((LANG_ENG, "English"), (LANG_KOR, "Korean"))
        
    
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    
    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))
    
    
    
    
    """ Variables """
    avatar = models.ImageField(upload_to = "avatars", null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True) 
    birthdate = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    language = models.CharField(choices=LANG_CHOICES, max_length=10, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=10, null=True, blank=True)
    superhost = models.BooleanField(default = False)
    
    
    #mail = models.EmailField3