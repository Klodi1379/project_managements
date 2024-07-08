from django import forms
from .models import Project, ProjectManager, Task
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'company', 'project_code', 'type', 'description', 'total_cost', 
                  'start_date', 'end_date', 'actual_start_date', 'actual_finish_date', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_start_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_finish_date': forms.DateInput(attrs={'type': 'date'}),
        }
        help_texts = {
            'start_date': 'The date when the project is planned to start.',
            'end_date': 'The date when the project is planned to finish.',
            'actual_start_date': 'The date when the project actually started. Leave blank if not started yet.',
            'actual_finish_date': 'The date when the project actually finished. Leave blank if not finished yet.',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        actual_start_date = cleaned_data.get("actual_start_date")
        actual_finish_date = cleaned_data.get("actual_finish_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be after start date.")
        
        if start_date and actual_start_date and start_date > actual_start_date:
            raise forms.ValidationError("Actual start date cannot be before the planned start date.")
        
        if end_date and actual_finish_date and end_date < actual_finish_date:
            raise forms.ValidationError("Actual finish date is after the planned end date. Please update the planned end date if the project is delayed.")
        
        if actual_start_date and actual_finish_date and actual_start_date > actual_finish_date:
            raise forms.ValidationError("Actual finish date must be after actual start date.")

        return cleaned_data

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'start_date', 'end_date', 'percent_complete', 'dependencies']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'dependencies': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].required = False
        if self.instance.pk:
            self.fields['dependencies'].queryset = Task.objects.exclude(pk=self.instance.pk)
        else:
            self.fields['dependencies'].queryset = Task.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        percent_complete = cleaned_data.get("percent_complete")
        project = cleaned_data.get("project")
        dependencies = cleaned_data.get("dependencies")

        if start_date and end_date and start_date > end_date:
            raise ValidationError("End date must be after start date.")

        if percent_complete is not None:
            if percent_complete < 0 or percent_complete > 100:
                raise ValidationError("Percent complete must be between 0 and 100.")

        if project and start_date and end_date:
            if start_date < project.start_date or end_date > project.end_date:
                raise ValidationError("Task dates must be within the project's start and end dates.")

        if dependencies:
            for dependency in dependencies:
                if dependency.end_date > start_date:
                    raise ValidationError(f"Dependency '{dependency.name}' ends after this task starts.")

        return cleaned_data

class ProjectProgressUpdateForm(forms.Form):
    percent_complete = forms.IntegerField(min_value=0, max_value=100)

class TaskProgressUpdateForm(forms.Form):
    percent_complete = forms.IntegerField(min_value=0, max_value=100)

class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ['user', 'project', 'role']

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get("user")
        project = cleaned_data.get("project")

        if ProjectManager.objects.filter(user=user, project=project).exists():
            raise forms.ValidationError("This user is already a manager for this project.")

        return cleaned_data