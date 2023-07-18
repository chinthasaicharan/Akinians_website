from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    phone = forms.CharField(max_length=12, required=True)

    class Meta:
        model = ContactUs
        fields = ['full_name', 'phone', 'email', 'message']


