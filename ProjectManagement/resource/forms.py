# resource/forms.py
from django import forms
from .models import Material, Equipment, Craft, SubContractor

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'description', 'unit', 'unit_cost', 'stock_quantity']

    def clean_unit_cost(self):
        unit_cost = self.cleaned_data.get('unit_cost')
        if unit_cost <= 0:
            raise forms.ValidationError("Unit cost must be greater than zero.")
        return unit_cost

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'description', 'model_number', 'manufacturer', 'rental_cost_per_day']

    def clean_rental_cost_per_day(self):
        rental_cost = self.cleaned_data.get('rental_cost_per_day')
        if rental_cost <= 0:
            raise forms.ValidationError("Rental cost must be greater than zero.")
        return rental_cost

class CraftForm(forms.ModelForm):
    class Meta:
        model = Craft
        fields = ['name', 'description', 'skill_level', 'hourly_rate']

    def clean_hourly_rate(self):
        hourly_rate = self.cleaned_data.get('hourly_rate')
        if hourly_rate <= 0:
            raise forms.ValidationError("Hourly rate must be greater than zero.")
        return hourly_rate

class SubContractorForm(forms.ModelForm):
    class Meta:
        model = SubContractor
        fields = ['name', 'contact_person', 'phone_number', 'email', 'specialization']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if SubContractor.objects.filter(email=email).exists():
            raise forms.ValidationError("A subcontractor with this email already exists.")
        return email