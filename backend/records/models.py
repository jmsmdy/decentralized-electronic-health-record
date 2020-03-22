from django.contrib.gis.db import models

from .choices import age_ranges, diseases, genders

class ConfirmedCase(models.Model):
    location = models.PointField()
    estimated_date_contracted = models.DateField('estimated date contracted')
    date_first_symptoms = models.DateField('date of first symptoms')
    date_confirmed = models.DateField('date confirmed')
    age_range = models.CharField(max_length=255, choices=age_ranges)
    genders = models.CharField(max_length=255, choices=genders)

class ContagionSite(models.Model):
    confirmed_case = models.ForeignKey(ConfirmedCase, on_delete=models.CASCADE)
    transmission_site = models.PointField()
    start_date = models.DateField('start time')
    end_date = models.DateField('end time')

class PreexistingConditionDatum(models.Model):
    confirmed_case = models.ForeignKey(ConfirmedCase, on_delete=models.CASCADE)
    disease = models.CharField(max_length=255, choices=diseases)
    status = models.CharField(max_length=255,
                              choices=[('yes', 'Yes'),
                                       ('no', 'No'),
                                       ('unknown', "I don't know")])
