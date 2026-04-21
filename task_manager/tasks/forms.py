from django import forms
from .models import Tasks
from task_manager.status.models import Statuses
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model

User = get_user_model()

class ExecutorChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, User):
        full_name = f"{User.last_name} {User.first_name}"
        return full_name


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
            empty_label="---------"
        )

    executor = ExecutorChoiceField(
            queryset=get_user_model().objects.all(),
            required=False,
            label='Исполнитель',
            widget=forms.Select(
                attrs={
                    'class': 'form-select',
                    'id': 'executor-select',
                }),
            empty_label="---------"
        )
    
    labels = forms.ModelMultipleChoiceField(
            queryset=Label.objects.all(),
            required=False,
            label='Метка',
            widget=forms.SelectMultiple(
                attrs={
                    'class': 'form-select',
                    'id': 'id_labels',
                })
        )
    
    author = forms.BooleanField(
            required=False,
            label='Только свои задачи',
            widget=forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                    'id': 'only-my-tasks-checkbox',
                }),
        )


class CreateTaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Statuses.objects.all(),
        empty_label="--------",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'status-select'}),
        label="Статус"
    )
    executor = ExecutorChoiceField(
        queryset=User.objects.all(),
        empty_label="--------",
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'executor-select'}),
        label="Исполнитель"

    )
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select', 'id': 'id_labels', 'size': '5'}),
        label="Метки"
    )
    
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
        }
        labels = {
            'task_name': 'Имя',
            'description': 'Описание',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)