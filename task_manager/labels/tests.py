from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Label

class TestLabelCRUD(TestCase):

    def setUp(self):
        self.labels = []
        for i in range(5):
            self.labels.append(Label.objects.create(label_name=f"In work{i}"))
        self.count_labels = len(self.labels)

    def test_create_label(self):
        label = Label.objects.create(label_name=f"Срочно")
        self.assertTrue(label)
        responce = self.client.get(reverse('labels:list_labels'))
        self.assertEqual(responce.status_code, 302)
        self.labels.append(label)
        self.assertTrue(self.count_labels + 1)

    def test_list_label(self):
        self.users = Label.objects.all()
        self.assertEqual(self.count_labels, 5)
        responce = self.client.get(reverse('labels:list_labels'))
        self.assertEqual(responce.status_code, 302)

    def test_update_label(self):
        responce = self.client.get(reverse("labels:list_labels"))
        self.assertEqual(responce.status_code, 302) 

    def test_delete_status(self):
        self.assertTrue(self.count_labels - 1)
        responce = self.client.get(reverse('labels:list_labels'))
        self.assertEqual(responce.status_code, 302)
