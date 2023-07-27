from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["title", "body"]
    list_filter = ["created"]
