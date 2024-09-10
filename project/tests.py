from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Client, Project
from django.contrib.auth.models import User

class ClientAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.force_authenticate(user=self.user)

        self.client_data = {'client_name': 'Nimap', 'created_by': self.user.id}
        self.client_instance = Client.objects.create(client_name='ClientA', created_by=self.user)
        self.project_data = {'project_name': 'Project A', 'client': self.client_instance.id, 'users': [self.user.id]}
        self.project_create_url = f'/clients/{self.client_instance.id}/projects/'
        self.project_list_url = '/projects/'

    def test_create_client(self):
        response = self.client.post('/clients/', self.client_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['client_name'], 'Nimap')

    def test_list_clients(self):
        self.client.post('/clients/', self.client_data, format='json')
        response = self.client.get('/clients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_client(self):
        client = Client.objects.create(client_name='Infotech', created_by=self.user)
        response = self.client.get(f'/clients/{client.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['client_name'], 'Infotech')

    def test_update_client(self):
        client = Client.objects.create(client_name='OldName', created_by=self.user)
        response = self.client.put(f'/clients/{client.id}/', {'client_name': 'NewName', 'created_by': self.user.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['client_name'], 'NewName')

    def test_delete_client(self):
        client = Client.objects.create(client_name='ToDelete', created_by=self.user)
        response = self.client.delete(f'/clients/{client.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_project(self):
        response = self.client.post(self.project_create_url, self.project_data, format='json')
        print(response.data)  # Debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['project_name'], 'Project A')

    def test_list_projects(self):
        # Ensure a project is created
        self.client.post(self.project_create_url, self.project_data, format='json')
        response = self.client.get(self.project_list_url)
        print(response.data)  # Debugging
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['project_name'], 'Project A')
