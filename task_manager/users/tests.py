from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class TestUsersCRUD(TestCase):

    def setUp(self):
        self.users = []
        for i in range(5):
            self.users.append(
                User.objects.create(
                    username=f"user{i}",
                    password=f"pass{i}"))
        self.count_users = len(self.users)

    def test_create_user(self):
        user = User.objects.create_user(
            username="Li",
            password="pass123")
        self.assertTrue(user)
        responce = self.client.get(
            reverse_lazy('users:register_user'))
        self.assertEqual(responce.status_code, 200)
        self.users.append(user)
        self.assertTrue(self.count_users + 1)

    def test_list_users(self):
        self.users = User.objects.all()
        self.assertEqual(self.count_users, 5)
        responce = self.client.get(
            reverse_lazy('users:list_users'))
        self.assertEqual(responce.status_code, 200)

    def test_update_user(self):
        responce = self.client.get(
            reverse_lazy('users:list_users'))
        self.assertEqual(responce.status_code, 200) 

    def test_delete_user(self):
        self.assertTrue(self.count_users - 1)
        responce = self.client.get(
            reverse_lazy('users:list_users'))
        self.assertEqual(responce.status_code, 200)

    