from django.test import RequestFactory, TestCase, Client
from .models import Quantity

# Create your tests here.
class QuantityTestCase(TestCase):

    def setUp(self):
        self.q = Quantity.objects.create(quantity=100)
    def test_quantity_is_equal_or_higher_than_0(self):
        quantity100 = Quantity.objects.get(quantity=100)
        self.assertIs(self.q,quantity100)