from django.contrib.gis import forms
from django.contrib.gis.forms import formset_factory
from leaflet.forms.fields import PointField, MultiPointField
from .widgets import XDSoftDateTimePickerInput




class ConfirmedCaseForm(forms.Form):
    location = PointField(
        label = 'Approximate Current Residence'
    )
    estimated_date_contracted = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(),
        label = 'Estimated Date Contracted'
    )
    date_confirmed = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'], 
        widget=XDSoftDateTimePickerInput(),
        label = 'Date Confirmed'
    )
    additional_info = forms.CharField(
        widget=forms.Textarea,
        label = 'Additional Information'
    )
    contagion_sites = MultiPointField(
        label='Locations Visited Since Contraction'
    )

class ContagionSiteForm(forms.Form):
    location = PointField(
        label='Possible Contagion Site'
    )
    start_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(),
        label = 'Start Time'
    )
    end_time = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=XDSoftDateTimePickerInput(),
        label = 'End Time'
    )


class SpaceTimeForm(forms.Form):
    location = PointField(
        label='Possible Contagion Site'
    )
    #time = forms.DateTimeField(
    #    input_formats=['%d/%m/%Y %H:%M'],
    #    widget=XDSoftDateTimePickerInput(),
    #    label = 'Date+Time'
    #)

SpaceTimeFormset = formset_factory(SpaceTimeForm, extra=1, can_delete=True)
