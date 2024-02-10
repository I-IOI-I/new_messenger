from django.contrib import admin

from chats.models import Message, BaseChat


@admin.register(BaseChat)
class Chat(admin.ModelAdmin):
    pass


@admin.register(Message)
class Message(admin.ModelAdmin):
    pass
