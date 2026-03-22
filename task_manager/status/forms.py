from django import forms
from .models import Statuses
from django.contrib.auth.forms import AuthenticationForm



class CreateStatusForm(forms.ModelForm):
    
    class Meta:

        model = Statuses
        fields = ["status_name"]
        widgets = {
            "status_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Название статуса",
                "autocomplete": "off"
            }),
        }
        labels = {
            "status_name": "Имя",
        }

