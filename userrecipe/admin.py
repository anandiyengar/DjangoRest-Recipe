from .models import DietModel, Recipe
from django.contrib import admin

# Register your models here.

admin.site.register(Recipe)
admin.site.register(DietModel)