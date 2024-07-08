# company/models.py
from django.db import models
from django.core.validators import RegexValidator
from core.models import TimeStampedModel, NamedModel, ContactInfoMixin
from core.utils import unique_slug_generator

class Company(TimeStampedModel, NamedModel, ContactInfoMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    register_name = models.CharField(max_length=255)
    address = models.TextField()
    post_code = models.CharField(max_length=10)
    fax_number = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name    


