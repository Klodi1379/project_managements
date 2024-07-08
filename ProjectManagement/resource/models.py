# resource/models.py
from django.db import models
from core.models import TimeStampedModel, NamedModel

class ResourceType(TimeStampedModel, NamedModel):
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

class Material(ResourceType):
    unit = models.CharField(max_length=50)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.unit})"

class Equipment(ResourceType):
    model_number = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    rental_cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)

class Craft(ResourceType):
    skill_level = models.CharField(max_length=50)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

class SubContractor(TimeStampedModel, NamedModel):
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    specialization = models.CharField(max_length=100)

