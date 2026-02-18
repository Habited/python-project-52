from django import forms
from django.contrib.auth.hashers import make_password
from task_manager.models import Users


class RegisterUserForm(forms.ModelForm):
    password_validation = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-input",
            "placeholder": "Подтверждение пароля",
            "autocomplite": "new_password"
        }),
        label="Подтверждение пароля",
        help_text="Для подтверждения введите, пожалуйста, пароль ещё раз.",
    )

    class Meta:
        model = Users
        fields = ["first_name", "last_name", "user_name", "password",]
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Имя",
                "autocomplite": "given_name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Фамилия",
                "autocomplite": "family_name"
            }),
            "user_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Имя пользователя",
                "autocomplite": "user_name"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-input",
                "placeholder": "Пароль",
                "autocomplite": "new_password"
            }),
        }
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "user_name": "Имя пользователя",
            "password": "Пароль"
        }
        help_texts = {
            "user_name": "Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.",
            "password": "Ваш пароль должен содержать как минимум 3 символа.",
        }


class LoginUserForm(forms.ModelForm):
    
    class Meta:
        model = Users
        fields = ["user_name", "password"]
        widgets = {
            "user_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Имя пользователя",
                "autocomplite": "user_name"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-input",
                "placeholder": "Пароль",
                "autocomplite": "new_password"
            }),
        }
        labels = {
            "user_name": "Имя пользователя",
            "password": "Пароль"
        }