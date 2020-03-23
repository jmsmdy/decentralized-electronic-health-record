from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import ConfirmedCase, ContagionSite

@admin.register(ConfirmedCase)
class ConfirmedCaseAdmin(OSMGeoAdmin):
    list_display = ['estimated_date_contracted',
                    'date_first_symptoms',
                    'date_confirmed',
                    'age_range',
                    'gender',
                    'additional_info']

@admin.register(ContagionSite)
class ContagionSiteAdmin(OSMGeoAdmin):
    list_display = ['confirmed_case', 'transmission_site', 'start_date', 'end_date']
