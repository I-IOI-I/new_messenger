from django.contrib import admin

from chats.models import *


@admin.register(DirectChat)
class DirectChat(admin.ModelAdmin):
    pass


@admin.register(GroupChat)
class GroupChat(admin.ModelAdmin):
    pass


@admin.register(Channel)
class Channel(admin.ModelAdmin):
    pass


@admin.register(ChatMember)
class ChatMember(admin.ModelAdmin):
    pass


@admin.register(Message)
class Message(admin.ModelAdmin):
    pass
