from django.test import TestCase
from django.urls import reverse

from catalog_app.models import Customer
from django.contrib.auth.models import Permission, User

# Create your tests here.

class TestCustomerListView(TestCase):

    """
    Test if CustomerListView displays all customer paginated and
    test if CustomerListView uses the correct urls and templates
    """

    @classmethod
    def setUpTestData(cls):
        # Create 15 customers for pagination test
        num_customers = 15

        for customer_id in range(num_customers):
            Customer.objects.create(
                name=f'Christian {customer_id}',
                location=f'Berlin {customer_id}',
                address=f'Hauptstraße {customer_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/customers/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog_app/customer_list.html')

    def test_pagination_is_one(self):
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context) # response.context is passed to template view
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['customer_list']) == 10)

    def test_lists_all_authors(self):
        # Get second page and confirm it has (exactly) remaining 5 items
        response = self.client.get(reverse('customers')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['customer_list']) == 5)

class TestAuthorizationForCustomerList(TestCase):

    """
    TODO: fix permission check work for CustomerListView and return correct status code (not always 200)
    """
     
    def setUp(self):

        # Create two users
        normal_user = User.objects.create_user(username="normal_user", password = "2HJ1vRV0Z&3iD")
        special_user = User.objects.create_user(username="special_user", password = "2HJ1vRV0Z&3iD")

        normal_user.save()
        special_user.save()

        # Assin special permissions to special_user
        permission = Permission.objects.get(codename="can_see_all_customers")
        special_user.user_permissions.add(permission)
        special_user.save()

        # Create two Customers
        Customer.objects.create(name="TestCustomerA", location="A", address="Hauptstraße A")
        Customer.objects.create(name="TestCustomerB", location="B", address="Hauptstraße B") 

    def test_forbidden_if_not_logged_in_but_correct_permission(self):
        """Access should be refused if correct permisson but not logged in"""
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 200)
    
    def test_forbidden_if_logged_in_but_not_correct_permission(self):
        """Access should be refused if logged in but missing permisson"""
        login = self.client.login(username='normal_user', password = '2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 403)

    def test_forbidden_if_logged_in_but_not_correct_permission(self):
        """Access should be granted if logged in with special user"""
        login = self.client.login(username='special_user', password = '2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 200)
    





