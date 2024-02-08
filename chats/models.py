from django.db import models
from django.contrib.auth.models import User
from core.models import UserProfile


class BaseChat(models.Model):
    dc = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField('core.UserProfile', through='ChatMember')

    class Meta:
        abstract = True


class DirectChat(BaseChat):
    user1 = models.ForeignKey('core.UserProfile', on_delete=models.SET_NULL)
    user2 = models.ForeignKey('core.UserProfile', on_delete=models.SET_NULL)


class GroupChat(BaseChat):
    dc = models.DateTimeField(auto_now_add=True)
    admins = models.ManyToManyField('core.UserProfile')


name = models.CharField(max_length=255)


class ChatMember(models.Model):
    ROLES_CHOICES = [
        ("Member", "Member"),
        ("Admin", "Admin"),
    ]

    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="chats_member"
    )

    chat = models.ForeignKey(
        BaseChat,
        on_delete=models.CASCADE,
        related_name="members"
    )

    role = models.CharField(
        max_length=9,
        choices=ROLES_CHOICES
    )

    def __str__(self):
        return f"{self.user_profile.user.username} {self.chat.name}"