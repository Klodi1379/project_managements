from django.db import models
from django.core.exceptions import ValidationError
from project.models import Project
from resource.models import Material, Equipment
from employee_management.models import Employee

class ResourceAllocation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date must be after start date.")
        if self.start_date < self.project.start_date or self.end_date > self.project.end_date:
            raise ValidationError("Allocation dates must be within project timeline.")

class MaterialAllocation(ResourceAllocation):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='material_allocations')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.material.name} allocated to {self.project.name}"

class EquipmentAllocation(ResourceAllocation):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='equipment_allocations')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.equipment.name} allocated to {self.project.name}"

class EmployeeAllocation(ResourceAllocation):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='employee_allocations')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.user.get_full_name()} allocated to {self.project.name}"