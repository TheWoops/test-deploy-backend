from django.test import TestCase
from catalog_app.models import Customer

# Create your tests here.

class CustomerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """All tests in this class are executed with this instance of customer"""
        Customer.objects.create(name="TestCustomer", location="Berlin", address="Hauptstraße 23")

    def test_name_label(self):
        '''Test if attribute name has the correct label assigned'''
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name # _meta to get instance of field name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        """Test if length of attribute name is 100"""
        customer = Customer.objects.get(id=1)
        field_length = customer._meta.get_field('name').max_length
        self.assertEqual(field_length, 100)

    def test_str_dunder_method(self):
        """Test if str dunder method returns the correct customer name"""
        customer = Customer.objects.get(id=1)
        expected_object_name = f'{customer.name}'
        self.assertEqual( expected_object_name, str(customer))

    def test_get_absolute_url(self):
        """Test if method returns correct url to customer detail view"""
        customer = Customer.objects.get(id=1)
        self.assertEqual(customer.get_absolute_url(), '/catalog/customer/1')


class MyTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        '''Called before every test function'''

        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def tearDown(self):
        print("Tear down.")
