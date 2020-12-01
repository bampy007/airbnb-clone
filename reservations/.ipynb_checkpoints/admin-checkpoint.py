from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        "room", "guest", "status", "check_in", "check_out",
        "in_progress", "is_finished",
    )

    list_filter = ("status",)

    # 함수는 필터링이 아직은 안되네 
    #list_filter = ("in_progress", "is_finished",)