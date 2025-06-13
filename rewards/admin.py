from django.contrib import admin
from django.utils.html import format_html

from rewards.models import Achievement, Badge

# Register your models here.
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description','badgeImage_view','points_needed')
    list_filter = ('name',)
    search_fields = ('name',)

    def badgeImage_view(self, obj):
        full_url = f"http://localhost:8000/media/{obj.badgeImage}"
        return  format_html('<img src="{}" height="100px" width="100px"/>', full_url)


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description','achievementImage_view')
    list_filter = ('name',)
    search_fields = ('name',)

    def achievementImage_view(self, obj):
        full_url = f"http://localhost:8000/media/{obj.achievementImage}"
        return format_html('<img src="{full_url}" height="100px" width="100px"/>', full_url)



admin.site.register(Achievement, AchievementAdmin)

admin.site.register(Badge, BadgeAdmin)