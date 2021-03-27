from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    """Class containing typical information about our customers"""

    name = models.CharField(max_length=100, help_text='e.g. Microsoft Deutschland GmbH')
    location = models.CharField(max_length=70, blank=True, default = '', help_text='e.g. Stuttgart')
    address = models.CharField(max_length=250, 
        help_text='e.g. Meitnerstraße 9, 70563 Stuttgart',
        blank=True,
        default = '')

    class Meta:
       ordering = ['name', 'location']
       permissions = (("can_see_all_customers", "Can see all customers"),)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('customer-detail', args=[str(self.id)])


class System(models.Model):
    """Class representing systems a customer has"""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) # if customer deleted, delete systems too
    protocol = models.CharField(max_length=5, default="https", help_text='e.g. https')
    host = models.CharField(max_length=150, help_text='e.g. 127.0.0.1')
    suffix = models.CharField(max_length=200, blank=True,  default = '', help_text='e.g. 127.0.0.1')
    port = models.CharField(max_length=5, default = '443', help_text='e.g. 443')
    user = models.CharField(max_length=20, blank=True, default = '', help_text='username to access system')
    password = models.CharField(max_length=30, blank=True, default = '', help_text='password to access system')
    token = models.CharField(max_length=255, blank=True, default = '', help_text='OATH Token to access system')

    class Meta:
        ordering = ['customer', 'host']
        permissions = (("can_see_all_systems", "Can see all systems"),)

    def __str__(self):
        return f'{self.customer.name} | {self.protocol}://{self.host}:{self.port}/{self.suffix}'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('system-detail', args=[str(self.id)])







