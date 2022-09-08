from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validation_if_number_is_positive(number: int):
    if number < 0:
        raise ValidationError(
            _(f'{number} isn\' positive'),
            params={'number': number}
        )
