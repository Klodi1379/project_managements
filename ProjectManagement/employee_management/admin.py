# user/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Employee

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'Employee Information'

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'groups')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('role', 'date_of_birth', 'address', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('role', 'date_of_birth', 'address', 'phone_number')}),
    )
    inlines = [EmployeeInline]

admin.site.register(User, CustomUserAdmin)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department', 'position', 'hire_date')
    list_filter = ('department', 'position')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'employee_id')