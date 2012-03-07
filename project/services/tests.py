from django.test import TestCase

from .models import Service


class ServicesModelTestCase(TestCase):

    def test_should_have_name_field(self):
        self.assertFieldIn('name', Service)

    def assertFieldIn(self, field_name, model):
        self.assertTrue(model._meta.get_field(field_name))
