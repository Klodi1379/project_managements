from django import forms
from .models import MaterialAllocation, EquipmentAllocation, EmployeeAllocation

class ResourceAllocationForm(forms.ModelForm):
    class Meta:
        fields = ['project', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class MaterialAllocationForm(ResourceAllocationForm):
    class Meta(ResourceAllocationForm.Meta):
        model = MaterialAllocation
        fields = ResourceAllocationForm.Meta.fields + ['material', 'quantity']

class EquipmentAllocationForm(ResourceAllocationForm):
    class Meta(ResourceAllocationForm.Meta):
        model = EquipmentAllocation
        fields = ResourceAllocationForm.Meta.fields + ['equipment']

class EmployeeAllocationForm(ResourceAllocationForm):
    class Meta(ResourceAllocationForm.Meta):
        model = EmployeeAllocation
        fields = ResourceAllocationForm.Meta.fields + ['employee']