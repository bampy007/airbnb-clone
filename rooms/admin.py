from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    



#inline Admin 
#class PhotoInline(admin.TabularInline):
class PhotoInline(admin.StackedInline):
  
    model = models.Photo
    
    

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    
    inlines = (PhotoInline,)
    
    
    fieldsets = (
        (
            "Basic Info", 
            {"fields": ("name", "description", "country", "city", "address", "price") 
            }, 
        ),
        
        (   "TImes",
             {"fields": ("check_in", "check_out", "instant_book") 
             }
        ),
       
        (   "More About the Space", 
             {  "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules") 
             }, 
        ),
        (   "Spaces", 
             {"fields": ("guests", "beds", "bedrooms", "baths") 
             },
        ),
        (   "Last Details", 
             {"fields": ("host", "room_type")
             },
        ),
        
    )
    
    
    list_display = (
        #variable
        "name", "country","city","price",
        "guests","beds","baths",
        "check_in","check_out","instant_book",
        
        #function
        "count_amenities","count_photos","total_rating",
    )
    
    ordering = ('name', 'price',)
        
    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    
    #radw_id
    raw_id_fields = ("host", )
    
    #search field 추가      #host __ username : __ 하위 변수 접근 방법
    search_fields = ("^city", "host__username")   
    
    #filter style 설정
    filter_horizontal =  (
        "amenities",
        "facilities",
        "house_rules",
    )
    
    # 요고는 어케 동작하는지 아직 잘 모르겠네. 오버라이딩이고, #어드민을 컨트롤 어떻게?
    def save_model(self, request, obj, form, change):
        print(obj, change, form)
        super().save_model(request, obj, form, change)   #call the real save() method
        print("room admin- save model")
    
    
    def count_amenities(self, obj):
        return obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"
    
    pass



@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ("__str__", "get_thumnail")
        
    def get_thumnail(self, obj):
        print(dir(obj.file))
        print( obj.file.url )
        return mark_safe(f'<img width="100px" src="{obj.file.url}" />') #it doesnt works - security issue - 
        
