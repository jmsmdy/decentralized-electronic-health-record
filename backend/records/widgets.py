from django.contrib.gis import forms
from django.forms.widgets import Input

class XDSoftDateTimePickerInput(forms.DateTimeInput):
    template_name = 'records/widgets/xdsoft_datetimepicker.html'

class PointPicker(Input):
    template_name = 'records/widgets/pointpicker.html'
