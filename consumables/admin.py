from django.contrib import admin
from django.utils.html import format_html

from consumables.models import FoodItem, Recipe


# Register your models here.

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name','calories','objectiveType','kind','foodPicture_view')

    list_filter = ('name','kind','objectiveType')
    list_ordered = ('calories',)

    def foodPicture_view(self, obj):
        full_url = f"http://localhost:8000/media/{obj.foodPicture}"
        return format_html('<img src="{}" height="250px" width="250px"/>', full_url)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','totalCalories','kind','objectiveType','recipeImage_view')
    list_filter = ('name','kind','objectiveType')
    list_ordered = ('calories',)

    def recipeImage_view(self, obj):
        full_url = f"http://localhost:8000/media/{obj.recipeImage}"
        return format_html('<img src="{}" height="250px" width="250px"/>', full_url)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(FoodItem,FoodItemAdmin)