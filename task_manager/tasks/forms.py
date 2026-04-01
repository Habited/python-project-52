from django import forms
from .models import Tasks
from task_manager.status.models import Statuses
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model


class ListTasksForm(forms.Form):

    status = forms.ModelChoiceField(
            queryset=Statuses.objects.all(),
            required=False,
            label='Статус',
            widget=forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'status-select',
                }),
            empty_label="Все статусы"
        )

    executor = forms.ModelChoiceField(
            queryset=get_user_model().objects.all(),
            required=False,
            label='Исполнитель',
            widget=forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'executor-select',
                }),
            empty_label="Все исполнители"
        )
    
    labels = forms.ModelChoiceField(
            queryset=Label.objects.all(),
            required=False,
            label='Метка',
            widget=forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'labels-select',
                }),
            empty_label="Все Метки"
        )



class CreateTaskForm(forms.ModelForm):
    
    class Meta:

        model = Tasks
        fields = ["task_name", "description", "status", "executor", "labels"]
        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'task_name-input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'maxlength': 5000
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
                'id': 'status-select',
            }),
            'executor': forms.Select(attrs={
                'class': 'form-select',
                'id': 'executor-select',
            }),
            'labels': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'id': 'labels-select',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].empty_label = "--------"
        self.fields['status'].queryset = Statuses.objects.all()
        self.fields['executor'].empty_label = "--------"
        self.fields['executor'].queryset = get_user_model().objects.all()
        self.fields['labels'].queryset = Label.objects.all()