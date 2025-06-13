from django.contrib import admin

from customers.models import Customer

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id','kind','points','gender','height','weight','age','user__username','user__first_name','user__last_name','user__email')
    list_select_related = True
    search_fields = ('user__username','kind')
    list_filter = ('points','gender','age','kind')

admin.site.register(Customer,CustomerAdmin)