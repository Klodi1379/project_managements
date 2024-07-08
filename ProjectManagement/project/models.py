from django.db import models
from django.core.exceptions import ValidationError
from core.models import TimeStampedModel, NamedModel
from company.models import Company
from employee_management.models import User
from django.utils import timezone

class Project(TimeStampedModel, NamedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project_code = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    total_cost = models.DecimalField(max_digits=15, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    actual_finish_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, default='PLANNING')
    percent_complete = models.IntegerField(default=0)

    class Meta:
        ordering = ['-start_date']  # Changed from 'plan_start_date' to 'start_date'

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError("End date must be after start date.")
        
        if self.start_date and self.actual_start_date and self.start_date > self.actual_start_date:
            raise ValidationError("Actual start date cannot be before the planned start date.")
        
        if self.end_date and self.actual_finish_date and self.end_date < self.actual_finish_date:
            raise ValidationError("Actual finish date cannot be after the planned end date.")
        
        if self.actual_start_date and self.actual_finish_date and self.actual_start_date > self.actual_finish_date:
            raise ValidationError("Actual finish date must be after actual start date.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def is_completed(self):
        return self.actual_finish_date is not None
    
    @property
    def progress_percentage(self):
        if self.status == 'COMPLETED':
            return 100
        elif self.status == 'NOT_STARTED':
            return 0
        else:
            total_days = (self.end_date - self.start_date).days
            days_passed = (timezone.now().date() - self.start_date).days
            if total_days > 0:
                return min(100, max(0, (days_passed / total_days) * 100))
            return 0
        
    @property
    def duration(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days
        return None

    def update_progress(self, percent):
        self.percent_complete = percent
        self.save()

class ProjectManager(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='managers')
    role = models.CharField(max_length=50)

    class Meta:
        unique_together = ('user', 'project')

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.project.name} - {self.role}"

class Task(TimeStampedModel, NamedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    start_date = models.DateField()
    end_date = models.DateField()
    percent_complete = models.IntegerField(default=0)
    dependencies = models.ManyToManyField('self', symmetrical=False, blank=True)

    @property
    def duration(self):
        return (self.end_date - self.start_date).days
    
    def update_progress(self, percent):
        self.percent_complete = percent
        self.save()

    def __str__(self):
        return f"{self.name} - {self.project.name}"