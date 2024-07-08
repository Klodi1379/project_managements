# control/models.py
from django.db import models
from django.core.exceptions import ValidationError
from core.models import TimeStampedModel
from project.models import Project
from resource.models import Material, Equipment, Craft, SubContractor

class ControlObject(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='control_objects')
    code = models.CharField(max_length=50)
    description = models.TextField()
    planned_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    actual_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=50)
    planned_start_date = models.DateField()
    planned_finish_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    actual_finish_date = models.DateField(null=True, blank=True)
    total_float = models.DecimalField(max_digits=10, decimal_places=2)
    threshold_time = models.DecimalField(max_digits=10, decimal_places=2)
    threshold_cost = models.DecimalField(max_digits=15, decimal_places=2)
    site_condition = models.CharField(max_length=255)
    weather = models.CharField(max_length=255)
    congestion = models.CharField(max_length=255)

    class Meta:
        unique_together = ('project', 'code')

    def clean(self):
        if self.planned_finish_date <= self.planned_start_date:
            raise ValidationError("Planned finish date must be after planned start date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def progress_percentage(self):
        if self.planned_quantity > 0:
            return (self.actual_quantity / self.planned_quantity) * 100
        return 0

class Predecessor(TimeStampedModel):
    control_object = models.ForeignKey(ControlObject, on_delete=models.CASCADE, related_name='predecessors')
    predecessor = models.ForeignKey(ControlObject, on_delete=models.CASCADE, related_name='successors')
    lag = models.IntegerField(default=0)  # In days

    class Meta:
        unique_together = ('control_object', 'predecessor')

class Allocation(TimeStampedModel):
    control_object = models.ForeignKey(ControlObject, on_delete=models.CASCADE, related_name='allocations')
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True, blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True)
    craft = models.ForeignKey(Craft, on_delete=models.SET_NULL, null=True, blank=True)
    sub_contractor = models.ForeignKey(SubContractor, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=15, decimal_places=2)

class Progress(TimeStampedModel):
    control_object = models.ForeignKey(ControlObject, on_delete=models.CASCADE, related_name='progress_records')
    date = models.DateField()
    quantity_completed = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('control_object', 'date')