from django import forms
from .models import Statuses



class CreateStatusForm(forms.ModelForm):
    
    class Meta:

        model = Statuses
        fields = ["status_name"]
        widgets = {
            "status_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название статуса",
                "autocomplete": "off"
            }),
        }
        labels = {
            "status_name": "Имя",
        }

