from django.contrib import admin
from django.db import models
from django.utils.html import mark_safe
from core.models import UserProfile


@admin.register(UserProfile)
class UserProfile(admin.ModelAdmin):
    list_display = ['user', 'display_photo']
    readonly_fields = ['display_photo']

    def display_photo(self, obj):
        # Метод для отображения изображения профиля
        return mark_safe(f'<img src="{obj.photo.url}" width="50" />')

    display_photo.allow_tags = True
    display_photo.short_description = 'фото профиля'

    formfield_overrides = {
        models.ImageField: {'widget': admin.widgets.AdminFileWidget},
    }
