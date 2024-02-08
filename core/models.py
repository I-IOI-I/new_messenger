from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    STATUSES_CHOICES = [
        ("Online", "Online"),
        ("Offline", "Offline"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )
    status = models.CharField(
        max_length=7,
        choices=STATUSES_CHOICES
    )
    # avatart  ...

    def __str__(self):
        return self.user.username

    def get_status(self):
        return self.status

