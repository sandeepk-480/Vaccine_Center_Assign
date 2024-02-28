from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from app.models import VaccinationSlot, VaccinationCenter

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class VaccinationSlotForm(forms.ModelForm):
    class Meta:
      model = VaccinationSlot
      fields = ['id', 'name','phone_number', 'date']
      widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
      

class VaccinationCenterForm(forms.ModelForm):
    class Meta:
        model = VaccinationCenter
        fields = ['id', 'name', 'address', 'working_hours']