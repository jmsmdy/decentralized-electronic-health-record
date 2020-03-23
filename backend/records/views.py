from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize

from .forms import ConfirmedCaseForm, ContagionSiteForm, ContagionSiteFormset
from .models import ConfirmedCase, ContagionSite, PreexistingConditionDatum
from .choices import diseases

def index(request):
    return HttpResponse("Recorcds Index")

def confirmed(request):
    if request.method == 'POST':
        form = ConfirmedCaseForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/records/')
    else:
        form = ConfirmedCaseForm()
    return render(request, 'records/confirmed_case.html', {'form' : form})

def add_contagion_site(request, confirmed_case_id):
    if request.method == 'POST':
        form = ContagionSiteForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['finished'] == False:
                return HttpResponseRedirect(f'/records/add_contagion_site/{confirmed_case_id}')
            else:
                return HttpResponseRedirect('/records/map')
    else:
        form = ContagionSiteForm()
    return render(request, 'records/add_contagion_site.html',
                  {'form' : form,
                   'confirmed_case_id' : confirmed_case_id})


def process(form_data, formset_data):
    case = ConfirmedCase(
        estimated_date_contracted = form_data['estimated_date_contracted'],
        date_first_symptoms = form_data['date_first_symptoms'],
        date_confirmed = form_data['date_confirmed'],
        age_range = form_data['age_range'],
        gender = form_data['gender'],
        additional_info = form_data['additional_info']
    )
    case.save()
    disease_answers = form_data['diseases'].split('---')
    for i in range(len(diseases)):
        ped = PreexistingConditionDatum(
            confirmed_case = case,
            disease = diseases[i][0],
            status = disease_answers[i]
        )
        ped.save()
    for subform_data in formset_data:
        cs = ContagionSite(
            confirmed_case = case,
            transmission_site = subform_data['location'],
            start_date = subform_data['start_date'],
            end_date = subform_data['end_date']
        )
        cs.save()


def submit(request):
    template_name = 'records/submit.html'
    heading_message = 'Submit COVID-19 Case'
    if request.method == 'GET':
        form = ConfirmedCaseForm(request.GET or None)
        formset = ContagionSiteFormset(request.GET or None)
    elif request.method == 'POST':
        form = ConfirmedCaseForm(request.POST)
        formset = ContagionSiteFormset(request.POST)
        print(form.is_valid(), formset.is_valid())
        if form.is_valid() & formset.is_valid():
            print(form.cleaned_data)
            for subform in formset.cleaned_data:
                print(subform)
            process(form.cleaned_data, formset.cleaned_data)
            return HttpResponseRedirect('/records/')
    return render(request, template_name, {
        'form' : form,
        'formset' : formset,
        'heading' : heading_message
    })

def map(request):
    sites = ContagionSite.objects.all()
    points = [site.transmission_site for site in sites]
    print(points)
    return render(request, 'records/map.html', {'queryset' : points})

def data(request):
    sites = ContagionSite.objects.all()
    points = [site.transmission_site for site in sites]
    points_as_geojson = serialize('geojson', sites, geometry_field='transmission_site')
    return HttpResponse(points_as_geojson, content_type='json')

