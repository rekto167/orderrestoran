from django.contrib import admin

# Register your models here.
from .models import MenuModel, MenuOrder


@admin.register(MenuOrder, MenuModel)
class DefaultAdmin(admin.ModelAdmin):
    pass
