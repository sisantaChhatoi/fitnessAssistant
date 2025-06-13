from django.contrib import admin
from django.utils.html import format_html

from exercises.models import Exercise

# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'toughnessLevel','duration','giphy_view')
    list_filter = ('toughnessLevel',)
    list_per_page = 20
    search_fields = ('name',)

    def giphy_view(self,exercise):
        full_url = f"http://localhost:8000/media/{exercise.giphy}"
        return format_html('<img src={} width="200" height="200" />',full_url)

    @admin.display(ordering='toughnessLevel')
    def duration(self,exercise):
        if exercise.toughnessLevel == 'H':
            return 60
        elif exercise.toughnessLevel == 'M':
            return 80
        else: return 100



admin.site.register(Exercise, ExerciseAdmin)