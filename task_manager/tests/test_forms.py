from django.test import TestCase

# Создайте ваши тесты здесь

import datetime
from django.utils import timezone
from task_manager.users.forms import RegisterUserForm, LoginUserForm

class RegisterUserFormTest(TestCase):

    def test_renew_form_date_field_label(self):
        form = RegisterUserForm()
        self.assertTrue(form.fields['password_validation'].label == None or form.fields['password_validation'].label == 'Подтверждение пароля')

    def test_renew_form_date_field_help_text(self):
        form = RegisterUserForm()
        self.assertEqual(form.fields['password_validation'].help_text,'Для подтверждения введите, пожалуйста, пароль ещё раз.')
