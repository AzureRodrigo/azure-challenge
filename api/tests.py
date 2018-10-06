from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from .models import Register
from .views import GetRegisterView, PostRegisterView


class TestPostRegisterView(TestCase):
    def setUp(self):
        self.eventRegister = Register.objects.create(name='TesteRegister',
                                                     cost=200.0,
                                                     is_entry=True)
        self.factory = APIRequestFactory()
        self.view = PostRegisterView.as_view()
        self.client = APIClient()
        self.data = {"tipo_de_registro": True,
                     "nome_do_registro": "TesteRegister",
                     "valor_em_reais": 200.0}

    def test_register_view_success_status_code(self):
        url = reverse('api:post_registers', kwargs={'pk': self.eventRegister.pk})
        request = self.factory.get(url)
        response = self.view(request, pk=self.eventRegister.pk)
        self.assertEquals(response.status_code, 200)

    def test_register_view_not_found_status_code(self):
        url = reverse('api:post_registers', kwargs={'pk': 99})
        request = self.factory.get(url)
        response = self.view(request, pk=99)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_register_post_success_status_code(self):
        url = reverse('api:get_registers')
        request = self.client.post(url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_register_post_failure_status_code(self):
        url = reverse('api:get_registers')
        request = self.client.post(url)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)


class TestGetRegisterView(TestCase):
    def setUp(self):
        self.eventRegister = Register.objects.all()
        self.factory = APIRequestFactory()
        self.view = GetRegisterView.as_view()
        self.client = APIClient()

    def test_register_view_success_status_code(self):
        url = reverse('api:get_registers', kwargs={'pk': self.eventRegister.pk})
        request = self.factory.get(url)
        response = self.view(request, pk=self.eventRegister.pk)
        self.assertEquals(response.status_code, 200)

    def test_register_view_not_found_status_code(self):
        url = reverse('api:post_registers', kwargs={'pk': 99})
        request = self.factory.get(url)
        response = self.view(request, pk=99)
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_register_get_success_status_code(self):
        url = reverse('api:post_registers', kwargs={'pk': self.eventRegister.pk})
        request = self.factory.get(url)
        response = self.view(request, pk=self.eventRegister.pk)
        self.assertEquals(response.status_code, 200)

    def test_register_get_failure_status_code(self):
        url = reverse('api:post_registers')
        request = self.client.post(url)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
