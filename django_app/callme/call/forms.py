from django import forms
from .models import CallRequest


class CallRequest(forms.ModelForm):
    class Meta:
        model = CallRequest
        fields = ['your_name', 'your_phone_number']
