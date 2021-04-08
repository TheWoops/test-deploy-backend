from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class UpdateCustomerForm(forms.Form):
    new_location = forms.CharField(help_text="Enter a new company location")

    def clean_new_location(self):
        data = self.cleaned_data['new_location']

        # Check is length is not longer than 15 letters
        if len(data) > 15:
            raise ValidationError(_('To long location name - max length allowed is 15'))

        return data