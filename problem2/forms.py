"""Model Forms of problem2 app."""

from django import forms

from .models import Fibo


class FiboForm(forms.ModelForm):
    """Model form taken from Fibo."""

    class Meta(object):
        """Bind with model Fibo.

        Only value_limit needed to avoid displaying the result of
        evensum as a form field in the template.
        """

        model = Fibo
        fields = ['value_limit']
