from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'date', 'time', 'message']
        name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name',
                                                             'class': 'form-control'}))
        email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email',
                                                             'class': 'form-control'}))
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date','class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }
