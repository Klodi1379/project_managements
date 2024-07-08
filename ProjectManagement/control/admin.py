# control/admin.py
from django.contrib import admin
from .models import ControlObject, Predecessor, Allocation, Progress

class PredecessorInline(admin.TabularInline):
    model = Predecessor
    fk_name = 'control_object'
    extra = 1

class AllocationInline(admin.TabularInline):
    model = Allocation
    extra = 1

class ProgressInline(admin.TabularInline):
    model = Progress
    extra = 1

@admin.register(ControlObject)
class ControlObjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'project', 'description', 'planned_start_date', 'planned_finish_date', 'progress_percentage')
    list_filter = ('project', 'site_condition', 'weather')
    search_fields = ('code', 'description', 'project__name')
    inlines = [PredecessorInline, AllocationInline, ProgressInline]
    fieldsets = (
        (None, {
            'fields': ('project', 'code', 'description')
        }),
        ('Quantity', {
            'fields': ('planned_quantity', 'actual_quantity', 'unit')
        }),
        ('Dates', {
            'fields': ('planned_start_date', 'planned_finish_date', 'actual_start_date', 'actual_finish_date')
        }),
        ('Thresholds', {
            'fields': ('total_float', 'threshold_time', 'threshold_cost')
        }),
        ('Conditions', {
            'fields': ('site_condition', 'weather', 'congestion')
        }),
    )

    def progress_percentage(self, obj):
        return f"{obj.progress_percentage:.2f}%"
    progress_percentage.short_description = 'Progress'

@admin.register(Predecessor)
class PredecessorAdmin(admin.ModelAdmin):
    list_display = ('control_object', 'predecessor', 'lag')
    list_filter = ('control_object__project',)
    search_fields = ('control_object__code', 'predecessor__code')

@admin.register(Allocation)
class AllocationAdmin(admin.ModelAdmin):
    list_display = ('control_object', 'get_resource', 'quantity', 'cost')
    list_filter = ('control_object__project',)
    search_fields = ('control_object__code',)

    def get_resource(self, obj):
        return obj.material or obj.equipment or obj.craft or obj.sub_contractor
    get_resource.short_description = 'Resource'

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('control_object', 'date', 'quantity_completed')
    list_filter = ('control_object__project', 'date')
    search_fields = ('control_object__code',)
    date_hierarchy = 'date'