# user/models.py
from django.contrib.auth.models import AbstractUser, Group
from django.db import models

class User(AbstractUser):
    ROLES = [
        ('ADMIN', 'Administrator'),
        ('MANAGER', 'Project Manager'),
        ('EMPLOYEE', 'Employee'),
        ('CLIENT', 'Client'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLES)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # Add related_name to avoid clash with auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    
    
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            if self.role == 'ADMIN':
                group = Group.objects.get(name='Admin')
            elif self.role == 'MANAGER':
                group = Group.objects.get(name='Project Manager')
            elif self.role == 'EMPLOYEE':
                group = Group.objects.get(name='Employee')
            else:
                group = None
            
            if group:
                self.groups.add(group)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    hire_date = models.DateField()
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position}"