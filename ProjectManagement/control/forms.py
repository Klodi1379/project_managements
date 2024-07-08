# control/forms.py
from django import forms
from .models import ControlObject, Predecessor, Allocation, Progress

class ControlObjectForm(forms.ModelForm):
    class Meta:
        model = ControlObject
        fields = ['project', 'code', 'description', 'planned_quantity', 'actual_quantity', 'unit',
                  'planned_start_date', 'planned_finish_date', 'actual_start_date', 'actual_finish_date',
                  'total_float', 'threshold_time', 'threshold_cost', 'site_condition', 'weather', 'congestion']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'planned_start_date': forms.DateInput(attrs={'type': 'date'}),
            'planned_finish_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_start_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_finish_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        planned_start = cleaned_data.get('planned_start_date')
        planned_finish = cleaned_data.get('planned_finish_date')
        actual_start = cleaned_data.get('actual_start_date')
        actual_finish = cleaned_data.get('actual_finish_date')

        if planned_start and planned_finish and planned_start > planned_finish:
            raise forms.ValidationError("Planned finish date must be after planned start date.")
        
        if actual_start and actual_finish and actual_start > actual_finish:
            raise forms.ValidationError("Actual finish date must be after actual start date.")

        return cleaned_data

class PredecessorForm(forms.ModelForm):
    class Meta:
        model = Predecessor
        fields = ['control_object', 'predecessor', 'lag']

    def clean(self):
        cleaned_data = super().clean()
        control_object = cleaned_data.get('control_object')
        predecessor = cleaned_data.get('predecessor')

        if control_object == predecessor:
            raise forms.ValidationError("A control object cannot be its own predecessor.")

        return cleaned_data

class AllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['control_object', 'material', 'equipment', 'craft', 'sub_contractor', 'quantity', 'cost']

    def clean(self):
        cleaned_data = super().clean()
        resource_fields = ['material', 'equipment', 'craft', 'sub_contractor']
        resources = [cleaned_data.get(field) for field in resource_fields]
        
        if sum(1 for resource in resources if resource is not None) != 1:
            raise forms.ValidationError("Please select exactly one resource type.")

        return cleaned_data

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['control_object', 'date', 'quantity_completed', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_quantity_completed(self):
        quantity = self.cleaned_data.get('quantity_completed')
        if quantity < 0:
            raise forms.ValidationError("Quantity completed cannot be negative.")
        return quantity