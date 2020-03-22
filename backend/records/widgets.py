from django.contrib.gis import forms
from django.forms.widgets import Input

class XDSoftDateTimePickerInput(forms.DateInput):
    template_name = 'records/widgets/xdsoft_datetimepicker.html'

class XDSoftDatePickerInput(forms.DateInput):
    template_name = 'records/widgets/xdsoft_datepicker.html'

class BootstrapTextArea(Input):
    template_name = 'records/widgets/bootstrap_text_area.html'

class BootstrapSelect(forms.Select):
    input_type = 'select'
    template_name = 'records/widgets/bootstrap_select.html'
    option_template_name = 'django/forms/widgets/select_option.html'
    add_id_index = False
    checked_attribute = {'selected': True}
    option_inherits_attrs = False

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if self.allow_multiple_selected:
            context['widget']['attrs']['multiple'] = True
        return context

    @staticmethod
    def _choice_has_empty_value(choice):
        """Return True if the choice's value is empty string or None."""
        value, _ = choice
        return value is None or value == ''

    def use_required_attribute(self, initial):
        """
        Don't render 'required' if the first <option> has a value, as that's
        invalid HTML.
        """
        use_required_attribute = super().use_required_attribute(initial)
        # 'required' is always okay for <select multiple>.
        if self.allow_multiple_selected:
            return use_required_attribute

        first_choice = next(iter(self.choices), None)
        return use_required_attribute and first_choice is not None and self._choice_has_empty_value(first_choice)

class NamedRadio(forms.Select):

    template_name = 'records/widgets/bootstrap_select.html'

    def __init__(self, attrs=None, choices=(), radio_name=''):
        super().__init__(attrs=attrs, choices=choices)
        self.radio_name = radio_name

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['radio_name'] = self.radio_name
        return context


class BootstrapMultiBinaryRadio(forms.MultiWidget):
    template_name = 'records/widgets/bootstrap_multi_binary_radio.html'

    def __init__(self, attrs=None, options=()):
        widgets = []
        for option in options:
            widgets.append(
                NamedRadio(attrs=attrs, choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', "I don't know")], radio_name=option[1]),
            )
        super().__init__(widgets, attrs)
        self.num_widgets = len(options)

    def decompress(self, value):
        print(value)
        if isinstance(value, str):
            return value.split('---')
        return [None for i in range(self.num_widgets)]



class PointPicker(Input):
    template_name = 'records/widgets/pointpicker.html'
