from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from project.models import Project
from company.models import Company
from resource.models import Material, Equipment, Craft, SubContractor

class Command(BaseCommand):
    help = 'Creates default groups and permissions'

    def handle(self, *args, **options):
        # Create groups
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        project_manager_group, _ = Group.objects.get_or_create(name='Project Manager')
        employee_group, _ = Group.objects.get_or_create(name='Employee')

        # Define permissions for each group
        admin_permissions = Permission.objects.all()
        
        project_manager_permissions = [
            Permission.objects.get(codename='view_project'),
            Permission.objects.get(codename='add_project'),
            Permission.objects.get(codename='change_project'),
            Permission.objects.get(codename='view_company'),
            Permission.objects.get(codename='view_material'),
            Permission.objects.get(codename='view_equipment'),
            Permission.objects.get(codename='view_craft'),
            Permission.objects.get(codename='view_subcontractor'),
        ]
        
        employee_permissions = [
            Permission.objects.get(codename='view_project'),
            Permission.objects.get(codename='view_company'),
            Permission.objects.get(codename='view_material'),
            Permission.objects.get(codename='view_equipment'),
            Permission.objects.get(codename='view_craft'),
            Permission.objects.get(codename='view_subcontractor'),
        ]

        # Assign permissions to groups
        admin_group.permissions.set(admin_permissions)
        project_manager_group.permissions.set(project_manager_permissions)
        employee_group.permissions.set(employee_permissions)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))