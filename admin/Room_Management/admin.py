from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Room)



@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_type', 'facility_name', 'facility_image')
    search_fields = ('facility_name',)

