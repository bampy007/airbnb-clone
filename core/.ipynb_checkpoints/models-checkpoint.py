from django.db import models

# Create your models here.


#DB 등록을 원하지 않음. Meta class 사용할 것
class TimeStampedModel(models.Model):
    
    """Time stamped Model"""
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    #추가적인 정보
    class Meta:
        abstract = True
        
        