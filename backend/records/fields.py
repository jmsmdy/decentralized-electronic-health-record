from django.forms import MultiValueField, ChoiceField
from .widgets import BootstrapMultiBinaryRadio

class MultiBinaryField(MultiValueField):
    widget = BootstrapMultiBinaryRadio
    default_error_messages = {
        'invalid_date': 'Enter a valid date.',
        'invalid_time': 'Enter a valid time.',
    }

    def __init__(self, *, choices=None, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        localize = kwargs.get('localize', False)
        fields = tuple([ChoiceField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', "I don't know")]) for choice in choices])
        super().__init__(fields, **kwargs)

    def compress(self, data_list):
        if data_list:
            # Raise a validation error if time or date is empty
            # (possible if SplitDateTimeField has required=False).
            for data in data_list:
                if data in self.empty_values:
                    raise ValidationError(self.error_messages['invalid_date'], code='invalid_date')
            result = '---'.join(data_list)
            return result
        return None
