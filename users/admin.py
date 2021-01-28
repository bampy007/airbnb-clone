from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models



#admin을  models.User와 연결했는데 어케했는지 모르겠군.
#[1] decorator
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    list_display = (
        "username",
        "email",
        "gender",
        "language",
        "currency",
        "is_staff",
        "superhost",
        "email_verified",
        "email_secret",
        "login_method",
    )
    list_filter = (
            "language",
            "currency",
            "superhost",
            "is_staff")

#[2] alternative
#admin.site.register(models.User, CustomUserAdmin)



    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )
    