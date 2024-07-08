# project/admin.py
from django.contrib import admin
from .models import Project, ProjectManager

class ProjectManagerInline(admin.TabularInline):
    model = ProjectManager
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'project_code', 'type', 'status', 'start_date', 'end_date')
    list_filter = ('type', 'status', 'company')
    search_fields = ('name', 'project_code', 'company__name')
    inlines = [ProjectManagerInline]
    fieldsets = (
        (None, {
            'fields': ('name', 'company', 'project_code', 'type', 'description')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'actual_start_date', 'actual_finish_date')
        }),
        ('Financial', {
            'fields': ('total_cost',)
        }),
        ('Status', {
            'fields': ('status', 'percent_complete')
        }),
    )

    
    
    
