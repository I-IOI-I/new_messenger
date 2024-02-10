from django.db import models
from django.contrib.auth.models import AbstractUser

from core import consts


class User(AbstractUser):
    status = models.CharField(
        'Статус',
        max_length=255,
        choices=consts.USER_STATUS_CHOICES,
        default=consts.OFFLINE_STATUS,
    )

    friends = models.ManyToManyField('self')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.username

    def get_status(self):
        return self.status


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="user_profile"
    )

    photo = models.ImageField(
        'фото профиля',
        upload_to='profile_photos',
        blank=True,
        default='profile_photos/default.png',
    )

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'

    def __str__(self):
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'
        return self.user.username

# попытался унаследоваться от двух моделей с pk. При попытке создания миграции выдается ошибка:
# The field 'id' from parent model 'core.user' clashes with the field 'id' from parent model 'core.userprofile'.
# Так что так наследоваться нельзя
# class CombinationOfUserAndProfile(User, UserProfile):
#     pass
