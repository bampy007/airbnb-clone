from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from django.http import Http404
from django import forms


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(queryset=models.RoomType.objects.all())


class HomeView(ListView):

  """ HomeView Definition """    
  """ccbv.co.uk 참조"""
  pass

  model = models.Room
  paginate_by = 10
  paginate_orphans = 5
  ordering = "created"
  #context_object_name = "rooms"

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   now = timezone.now()
  #   context['nowTime'] = now

  #   return context


"""
[1] HttpResponse 로 url_request(HttpRequest) 에 대하여 응답
[2] render로 생성해낸 무엇으로 url_request 에 대하여 응답
"""

def room_detail(request, pk):
  #print(pk)

  try:
    room = models.Room.objects.get(pk=pk) 
    return render(request, "rooms/detail.html", {"room": room})
  except models.Room.DoesNotExist:
    raise Http404()
    #return redirect(reverse("core:home"))


#class RoomDetail(DetailView):

#""" RoomDetail Definition """

#model = models.Room

