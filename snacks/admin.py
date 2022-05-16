from django.contrib import admin

# Register your models here.

from .models import Snack


@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display=["title","purchaser","description"]
