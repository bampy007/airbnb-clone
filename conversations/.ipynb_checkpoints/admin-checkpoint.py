from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    
    list_display = (
        "__str__", "created", "user", "conversation",
    )

    list_filter = ("user",)

    

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
      list_display = (
        "__str__", "created", "count_messages", "count_participants",
    )

