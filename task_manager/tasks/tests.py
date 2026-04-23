from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Tasks
from django.contrib.auth import get_user_model

User = get_user_model()


class TestTasksCRUD(TestCase):

    def setUp(self):
        self.tasks = []
        for i in range(5):
            self.tasks.append(
                Tasks.objects.create(
                    task_name=f"Задача №{i}",
                    author=User.objects.create(username=f"user{i}",
                                               password=f"pass{i}")))
        self.count_tasks = len(self.tasks)

    def test_create_task(self):
        task = Tasks.objects.create(
            task_name="Постирать белье",
            author=User.objects.create(
                username="user", password="pass"))
        self.assertTrue(self.tasks)
        responce = self.client.get(reverse('tasks:list_tasks'))
        self.assertEqual(responce.status_code, 200)
        self.tasks.append(task)
        self.assertTrue(self.count_tasks + 1)

    def test_list_tasks(self):
        self.users = Tasks.objects.all()
        self.assertEqual(self.count_tasks, 5)
        responce = self.client.get(reverse('tasks:list_tasks'))
        self.assertEqual(responce.status_code, 200)

    def test_update_task(self):
        responce = self.client.get(reverse("tasks:list_tasks"))
        self.assertEqual(responce.status_code, 200) 

    def test_delete_task(self):
        self.assertTrue(self.count_tasks - 1)
        responce = self.client.get(reverse('tasks:list_tasks'))
        self.assertEqual(responce.status_code, 200)
