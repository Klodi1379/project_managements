# company/forms.py
from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'register_name', 'address', 'post_code', 'phone_number', 'fax_number', 'email', 'website']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'website': forms.URLInput(attrs={'placeholder': 'https://'}),
        }

    def clean_post_code(self):
        post_code = self.cleaned_data.get('post_code')
        # Add any specific post code validation logic here
        return post_code

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # Add phone number validation logic here
        return phone_number