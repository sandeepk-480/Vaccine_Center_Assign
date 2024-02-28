from django.contrib import admin
from app.models import VaccinationCenter, VaccinationSlot, DosageDetail

@admin.register(VaccinationCenter)
class VaccinationCenterAdmin(admin.ModelAdmin):
  list_display = ['name', 'working_hours']


@admin.register(VaccinationSlot)
class VaccinationSlotAdmin(admin.ModelAdmin):
  list_display = ['name', 'phone_number', 'date'] 


admin.site.register(DosageDetail)