from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(value):
    url_validator = URLValidator()
    value1_invalid = False
    value2_invalid = False
    try:
        url_validator(value)
    except:
        value1_invalid = True

    value2_url = "http://" + value
    try:
        url_validator(value2_url)
    except:
        value2_invalid = True

    if value1_invalid is False and value2_invalid is False:
        raise ValidationError("Invalid URL")
    return value


def validate_dot_com(value):
    if not ".com" in value:
        raise ValidationError("No .com in the URL")
