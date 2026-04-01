from django import forms
from .models import Label


class CreateLabelForm(forms.ModelForm):
    
    class Meta:

        model = Label
        fields = ["label_name"]
        widgets = {
            "label_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Название метки",
                "autocomplete": "off"
            }),
        }
        labels = {
            "label_name": "Имя",
        }
