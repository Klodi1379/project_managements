# user/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Employee

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'role', 'date_of_birth', 'address', 'phone_number')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = UserChangeForm.Meta.fields

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'employee_id', 'hire_date', 'department', 'position', 'wage', 'overtime_rate']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_employee_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if Employee.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError("This employee ID is already in use.")
        return employee_id