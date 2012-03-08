from django.test import TestCase

from .models import Service
from .api import ServiceResource


class SerivceResourceTestCase(TestCase):

    def test_should_use_a_service_queryset(self):
        self.assertEqual(Service, ServiceResource._meta.queryset.model)

    def test_resource_name_should_be_service(self):
        self.assertEqual('service', ServiceResource._meta.resource_name)


class ServicesModelTestCase(TestCase):

    def test_should_have_name_field(self):
        self.assertFieldIn('name', Service)

    def assertFieldIn(self, field_name, model):
        self.assertTrue(model._meta.get_field(field_name))
