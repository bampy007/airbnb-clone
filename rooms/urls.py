from django.urls import path        #dispatch <int:pk>
from rooms import views as room_views

from . import views

app_name = "rooms"

urlpatterns = [
    path("<int:pk>", views.room_detail, name="detail")
]
