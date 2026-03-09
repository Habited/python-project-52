from django.test import TestCase
from task_manager.models import Users


class UsersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = Users.objects.create(first_name="Dustin",
                                    last_name="Dollin",
                                    password="evka1247",
                                    password_validation="evka1247",
                                    time_create="12.02.2023 17:18")
        
    def test_first_name_verbose_name(self):
        user = Users.objects.get(pk=1)
        field_label = user._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "Имя")

    def test_first_name_max_lenght(self):
        user = Users.objects.get(pk=1)
        max_lenght = user._meta.get_field("first_name").max_length
        self.assertEqual(max_lenght, 255)

    def test_last_name_verbose_name(self):
        user = Users.objects.get(pk=1)
        field_label = user._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "Фамилия")

    def test_last_name_blank(self):
        user = Users.objects.get(pk=1)
        blank = user._meta.get_field("last_name").blank
        self.assertEqual(blank, True)

    def test_user_name_verbose_name(self):
        user = Users.objects.get(pk=1)
        field_label = user._meta.get_field("user_name").verbose_name
        self.assertEqual(field_label, "Имя пользователя")

    def test_user_name_blank(self):
        user = Users.objects.get(pk=1)
        blank = user._meta.get_field("user_name").blank
        self.assertEqual(blank, True)

    def test_password_verbose_name(self):
        user = Users.objects.get(pk=1)
        field_label = user._meta.get_field("password").verbose_name
        self.assertEqual(field_label, "Пароль")

    def test_password_blank(self):
        user = Users.objects.get(pk=1)
        blank = user._meta.get_field("password").blank
        self.assertEqual(blank, True)

    def test_password_max_lenght(self):
        user = Users.objects.get(pk=1)
        max_lenght = user._meta.get_field("password").max_length
        self.assertEqual(max_lenght, 255)

    def test_password_validation_verbose_name(self):
        user = Users.objects.get(pk=1)
        field_label = user._meta.get_field("password_validation").verbose_name
        self.assertEqual(field_label, "Подтвердить пароль")

    def test_password_validation_blank(self):
        user = Users.objects.get(pk=1)
        blank = user._meta.get_field("password_validation").blank
        self.assertEqual(blank, True)

    def test_password_validation_max_lenght(self):
        user = Users.objects.get(pk=1)
        max_lenght = user._meta.get_field("password_validation").max_length
        self.assertEqual(max_lenght, 255)

    def test_time_create_verbose_name(self):
        user = Users.objects.get(pk=1)
        field_label = user._meta.get_field("time_create").verbose_name
        self.assertEqual(field_label, "Дата регистрации")

    def test_time_create_auto_now_add(self):
        user = Users.objects.get(pk=1)
        auto_now_add = user._meta.get_field("time_create").auto_now_add
        self.assertEqual(auto_now_add, True)

    def test_get_absolute_url(self):
        user=Users.objects.get(pk=1)
        #self.assertEqual(user.get_absolute_url(), '/users/1')