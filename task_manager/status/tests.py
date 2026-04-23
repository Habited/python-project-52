from django.test import TestCase
from django.urls import reverse
from task_manager.status.models import Statuses


class TestUsersCRUD(TestCase):

    def setUp(self):
        self.statuses = []
        for i in range(5):
            self.statuses.append(
                Statuses.objects.create(
                    status_name=f"In work{i}"))
        self.count_statuses = len(self.statuses)

    def test_create_status(self):
        status = Statuses.objects.create(status_name="In work")
        self.assertTrue(status)
        responce = self.client.get(reverse('statuses:list_statuses'))
        self.assertEqual(responce.status_code, 302)
        self.statuses.append(status)
        self.assertTrue(self.count_statuses + 1)

    def test_list_statuses(self):
        self.users = Statuses.objects.all()
        self.assertEqual(self.count_statuses, 5)
        responce = self.client.get(reverse('statuses:list_statuses'))
        self.assertEqual(responce.status_code, 302)

    def test_update_status(self):
        responce = self.client.get(reverse("statuses:list_statuses"))
        self.assertEqual(responce.status_code, 302) 

    def test_delete_status(self):
        self.assertTrue(self.count_statuses - 1)
        responce = self.client.get(reverse('statuses:list_statuses'))
        self.assertEqual(responce.status_code, 302)
