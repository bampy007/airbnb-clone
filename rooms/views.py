from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

#def all_rooms(request):
##   print(dir(request))
#    now = datetime.now()
#    return HttpResponse(content=f"<h1> {now} </h1>")

#def all_rooms(request):
#    now = datetime.now()
#    hungry = True
    
#    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry }   )

def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "home.html", context={"room": all_rooms})
    