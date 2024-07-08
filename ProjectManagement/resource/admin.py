# resource/admin.py
from django.contrib import admin
from .models import Material, Equipment, Craft, SubContractor

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit', 'unit_cost', 'stock_quantity')
    list_filter = ('unit',)
    search_fields = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'model_number', 'manufacturer', 'rental_cost_per_day')
    list_filter = ('manufacturer',)
    search_fields = ('name', 'model_number', 'manufacturer')

@admin.register(Craft)
class CraftAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_level', 'hourly_rate')
    list_filter = ('skill_level',)
    search_fields = ('name',)

@admin.register(SubContractor)
class SubContractorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone_number', 'specialization')
    list_filter = ('specialization',)
    search_fields = ('name', 'contact_person', 'specialization')