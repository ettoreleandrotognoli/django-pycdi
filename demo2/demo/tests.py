from django.http import HttpRequest
from pycdi.core import CDIContainer
from django.shortcuts import resolve_url
from django.test import Client
from django.test import TestCase

from .views import MySingleton

DATA = 'some data'


class CDITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_without_injection(self):
        response = self.client.get(resolve_url('without-injection'))
        self.assertEqual(response.status_code, 200)

    def test_with_injection(self):
        response = self.client.get(resolve_url('with-injection', data=DATA))
        self.assertEqual(response.status_code, 200)
        context = response.context
        self.assertEqual(context['data'], DATA)
        self.assertEqual(context['url'], DATA)
        self.assertIsInstance(context['singleton'], MySingleton)
        self.assertIsInstance(context['kwargs']['random_number'], float)

    def test_with_request_injection(self):
        response = self.client.get(resolve_url('with-request-injection'))
        self.assertEqual(response.status_code, 200)
        context = response.context
        self.assertIsInstance(context['request'], HttpRequest)
        self.assertIsInstance(context['singleton'], MySingleton)
        self.assertIsInstance(context['random_number'], float)

    def test_container_inject(self):
        response = self.client.get(resolve_url('container-inject'))
        self.assertEqual(response.status_code, 200)
        context = response.context
        self.assertIsInstance(context['container'], CDIContainer)
        self.assertIsInstance(context['singleton'], MySingleton)
        self.assertIsInstance(context['number'], float)

    def test_generic_view(self):
        response = self.client.get(resolve_url('generic-view'))
        self.assertEqual(response.status_code, 200)
        context = response.context
        self.assertIsInstance(context['container'], CDIContainer)
        self.assertIsInstance(context['singleton'], MySingleton)
        self.assertIsInstance(context['number'], float)
        self.assertIsInstance(context['other_number'], float)
