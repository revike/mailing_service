from django.db import models


class LowerCaseEmailField(models.EmailField):
    """Email lower"""

    def get_prep_value(self, value):
        if value:
            return str(value).lower()
        return None
