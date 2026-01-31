from django import forms


class RegisterUserForm(forms.Form):
    first_name = forms.CharField(label="Имя", max_length=100)
    last_name = forms.CharField(label="Фамилия", max_length=100)
    username = forms.CharField(label="Имя пользователя", 
                               max_length=100, 
                               help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.")
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}), 
                               help_text="Ваш пароль должен содержать как минимум 3 символа.")
    password_validation = forms.CharField(label='Подтверждение пароля', 
                                          widget=forms.PasswordInput(attrs={'class': 'form-input'}), 
                                          help_text="Для подтверждения введите, пожалуйста, пароль ещё раз.")


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", 
                               max_length=100,)
    password = forms.CharField(label='Пароль', 
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}),)
