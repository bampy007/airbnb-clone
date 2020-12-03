from math import ceil
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
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

# def all_rooms(request):
#     #print(dir(request.GET.get("page", 0)))          # http://127.0.0.1:8000/?page=1
#     page = request.GET.get("page", 1)
#     page = int(page or 1)
#     page_size = 10   
#     limit = page_size * page
#     offset = limit - page_size
#     all_rooms = models.Room.objects.all()[offset:limit]   #변수생성 - context(수단)으로 html에게 전달
#     page_count = models.Room.objects.count() / page_size

#   #  print("all rooms :::::", all_rooms)
#     return render(request, "rooms/home.html",
#                  context={"rooms": all_rooms,
#                           "page" : page,
#                           "page_count" : ceil(page_count),
#                           "page_range" : range(1, ceil(page_count))})

def all_rooms(request):
    page = request.GET.get("page", 1)       #/?page=2
    room_list = models.Room.objects.all()   
    paginator = Paginator(room_list, 10)

    try:
      rooms_page = paginator.get_page(page)
      return render(request, "rooms/home.html", {"rooms": rooms_page})
    except EmptyPage:
      rooms_page = paginator.get_page(5)
      return redirect("/")
      
    

    #print(room_list) 
    #print(vars(rooms)) 
    #print(vars(rooms.paginator)) 
    


"""
[1] HttpResponse 로 url_request(HttpRequest) 에 대하여 응답
[2] render로 생성해낸 무엇으로 url_request 에 대하여 응답
"""