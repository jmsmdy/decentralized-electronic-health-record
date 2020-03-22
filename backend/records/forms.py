from django.contrib.gis import forms
from django.contrib.gis.forms import formset_factory
from leaflet.forms.fields import PointField, MultiPointField
from .widgets import XDSoftDateTimePickerInput, XDSoftDatePickerInput, BootstrapTextArea, BootstrapSelect, BootstrapMultiBinaryRadio
from .fields import MultiBinaryField

from .choices import age_ranges, genders, diseases, radii

class ConfirmedCaseForm(forms.Form):
    estimated_date_contracted = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'Estimated Date Contracted'
    )
    date_first_symptoms = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'Date of First Symptoms'
    )

    date_confirmed = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'Date Confirmed'
    )
    additional_info = forms.CharField(
        widget=BootstrapTextArea(),
        label = 'Additional Information',
        required=False
    )

    age_range = forms.ChoiceField(
        widget=BootstrapSelect(choices=age_ranges),
        choices=age_ranges
    )

    gender = forms.ChoiceField(
        widget=BootstrapSelect(choices=genders),
        choices=genders
    )

    diseases = MultiBinaryField(
        widget = BootstrapMultiBinaryRadio(options=diseases),
        choices = diseases
    )

class ContagionSiteForm(forms.Form):
    location = PointField(
        label='Possible Contagion Site'
    )
    start_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'START'
    )
    end_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'END'
    )
    radius = forms.ChoiceField(
        widget = BootstrapSelect(choices=radii),
        choices = radii
    )


ContagionSiteFormset = formset_factory(ContagionSiteForm, extra=1, can_delete=True)

class ConfirmedCaseFormOld(forms.Form):
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


class SpaceTimeForm(forms.Form):
    location = PointField(
        label='Possible Contagion Site'
    )
    start_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'START'
    )
    end_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=XDSoftDatePickerInput(),
        label = 'END'
    )


SpaceTimeFormset = formset_factory(SpaceTimeForm, extra=1, can_delete=True)
