from django.contrib import admin
from .models import Staff


# Register your models here.
#admin.site.register(Staff)
@admin.register(Staff)
class Staffadmin(admin.ModelAdmin):
    list_display = ('staffname', 'email', 'phone', 'address','status')
    