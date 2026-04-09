from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "password1", "password2"]
        
        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Имя",
                "autocomplete": "given-name"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Фамилия",
                "autocomplete": "family-name"
            }),
            "username": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Имя пользователя",
                "autocomplete": "username"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-input",
                "placeholder": "Пароль",
                "autocomplete": "new-password"
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-input",
                "placeholder": "Подтверждение пароля",
                "autocomplete": "new-password"
            }),
        }
        
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
            "username": "Имя пользователя",
            "password1": "Пароль",
            "password2": "Подтверждение пароля",
        }
        
        help_texts = {
            "username": "Обязательное поле. Не более 150 символов. Только буквы, цифры и @/./+/-/_.",
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        
        if commit:
            user.save()
        return user


class LoginUserForm(AuthenticationForm):
    
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={
            "class": "form-input",
            "placeholder": "Имя пользователя",
            "autocomplete": "username",
            "autofocus": True,
        }),
        max_length=150,
    )
    
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={
            "class": "form-input",
            "placeholder": "Пароль",
            "autocomplete": "current-password",
        }),
    )