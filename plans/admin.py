from django.contrib import admin

from plans.models import Plan, GeneratedPerDayPlan


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id','customer','created_at','completed_at','duration_in_days','completion_count')
    list_select_related = ('customer','customer__user')
    list_filter = ('customer','customer__user')
    list_per_page = 20
    ordering = ('-created_at','duration_in_days')

class GeneratedPerDayPlanAdmin(admin.ModelAdmin):
    list_display = ('id','plan','created_at','completed_at','day_no','completion_status')
    list_filter = ('plan','completed_at')

admin.site.register(GeneratedPerDayPlan,GeneratedPerDayPlanAdmin)
admin.site.register(Plan,PlanAdmin)
