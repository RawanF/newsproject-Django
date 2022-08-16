from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _


class TextValidator(RegexValidator):
    """
    a custom validator for only Arabic and English text
    """
    regex = r"^[\u0621-\u064A-a-zA-Z\ ]*$"
    message = _("It must contain Arabic or English letters only")
    # flags = 0


class IdValidator(RegexValidator):
    """
    a custom validator for national ID
    """
    regex = r"^[1][0-9]{9}\Z"
    message = _(
        'Enter a valid national ID'
    )
    # flags = 0
