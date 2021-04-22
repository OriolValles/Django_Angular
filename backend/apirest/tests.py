from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apirest.models import Printer
from rest_framework.test import force_authenticate

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


class PrinterTests(APITestCase):
    def test_create_Printer_without_user(self):
        """
        Ensure we can create a new Printer object.
        """
        url = reverse('printer-list')
        data = {'name': 'Printer1'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_Printer_with_user(self):
        """
        Ensure we can create a new Printer object.
        """
        client = APIClient()
        client.login(username='admin', password='password123')

        url = reverse('printer-list')
        data = {'name': 'Printer1'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Printer.objects.count(), 1)
        self.assertEqual(Printer.objects.get().name, 'Printer1')
        # Log out
        client.logout()