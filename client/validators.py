import re

import phonenumbers
from django.core.exceptions import ValidationError
from phonenumbers import NumberParseException


def validate_phone(value):
    """Validate for phone"""
    error = 'Invalid phone number format'
    try:
        pattern = r"^7\d{10,10}$"
        number = phonenumbers.parse(f'+{value}')
        if phonenumbers.is_valid_number(number) and re.search(pattern, value):
            return value
        raise ValidationError(error, params={'value': value})
    except NumberParseException:
        raise ValidationError(error, params={'value': value})
