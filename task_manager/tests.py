from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from task_manager.status.models import Statuses
from task_manager.tasks.models import Tasks

User = get_user_model()


class FullUserFlowTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.status = Statuses.objects.create(status_name='Новая')
    
    def test_full_flow(self):
        
        response = self.client.post(reverse('users:register_user'), {
            'username': 'flowuser',
            'password1': 'SecurePass123!',
            'password2': 'SecurePass123!',
            'email': 'flow@example.com',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(reverse('tasks:create_task'), {
            'task_name': 'Интеграционная задача',
            'description': 'Тест полного потока',
            'status': self.status.pk,
        }, follow=True)
        
        response = self.client.get(reverse('tasks:list_tasks'))
        self.assertEqual(response.status_code, 200)
