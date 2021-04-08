from django.test import TestCase
from catalog_app.forms import UpdateCustomerForm

# Create your tests here.

class TestUpdateCustomerForm(TestCase):

    def test_new_location_label(self):
        '''Test if attribute new_location has the correct label assigned'''
        form = UpdateCustomerForm()
        self.assertTrue(form.fields['new_location'].label == None or form.fields['new_location'].label == 'new_location')

    def test_new_location_help_text(self):
        """Test if help_text of new location attribute is correct"""
        form = UpdateCustomerForm()
        actual_help_text = form.fields['new_location'].help_text
        self.assertEqual(actual_help_text, "Enter a new company location")

    def test_clean_new_location(self):
        """Test if validation error is thrown if input longer 15 chars"""
        form = UpdateCustomerForm(data ={'new_location': "1234567891111110"})
        self.assertFalse(form.is_valid())

        """Test if NO validation error is thrown if input max. 15 chars"""
        form = UpdateCustomerForm(data ={'new_location': "123456789111111"})
        self.assertTrue(form.is_valid())
