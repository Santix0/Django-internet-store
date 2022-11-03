from django import forms
from django.forms.utils import ErrorList
from django_countries.fields import CountryField

from .models import Checkout

PAYMENT_OPTION = (
    ('S', 'Stripe'),
    ('P', 'PayPal'),
)
#


class CheckoutForm(forms.ModelForm):
    def __init__(
            self,
            data=None,
            files=None,
            auto_id="id_%s",
            prefix=None,
            initial=None,
            error_class=ErrorList,
            label_suffix=None,
            empty_permitted=False,
            instance=None,
            use_required_attribute=None,
            renderer=None,
    ):
        super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance,
                         use_required_attribute, renderer)
        self.user_id = None

    class Meta:
        model = Checkout
        fields = ['full_name', 'address', 'zip', 'country', 'phone']
        widgets = {
            'full_name': forms.TextInput(),
            'address': forms.TextInput(),
            'zip': forms.NumberInput(),
            'phone': forms.NumberInput(),
        }
