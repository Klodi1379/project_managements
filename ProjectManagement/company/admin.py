# company/admin.py
from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'register_name', 'phone_number', 'email', 'post_code')
    list_filter = ('post_code',)
    search_fields = ('name', 'register_name', 'email')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'register_name')
        }),
        ('Contact Information', {
            'fields': ('address', 'post_code', 'phone_number', 'fax_number', 'email', 'website')
        }),
    )
    
    
admin.site.register(Company, CompanyAdmin)