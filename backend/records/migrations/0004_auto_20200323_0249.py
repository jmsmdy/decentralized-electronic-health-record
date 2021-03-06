# Generated by Django 3.0.3 on 2020-03-23 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20200321_0520'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreexistingConditionDatum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(choices=[('asthma', 'Do you have asthma?'), ('cancer', 'Do you have cancer?'), ('coronary heart disease', 'Do you have coronary heart disease?'), ('diabetes', 'Do you have diabetes?'), (' hypertension', 'Do you have hypertension?'), ('hypertriglyceridemia', 'Do you have hypertriglyceridemia?'), ('prostate hypertrophy', 'Do you have prostate hypertropy (BPH)?')], max_length=255)),
                ('status', models.CharField(choices=[('yes', 'Yes'), ('no', 'No'), ('unknown', "I don't know")], max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='confirmedcase',
            name='location',
        ),
        migrations.AddField(
            model_name='confirmedcase',
            name='additional_info',
            field=models.CharField(blank=True, max_length=40000),
        ),
        migrations.AddField(
            model_name='confirmedcase',
            name='age_range',
            field=models.CharField(choices=[('0', '0-9'), ('10', '10-19'), ('20', '20-29'), ('30', '30-39'), ('40', '40-49'), ('50', '50-59'), ('60', '60-69'), ('70', '70-79'), ('80', '80-89'), ('90', '90+')], default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confirmedcase',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='male', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MedicalDatum',
        ),
        migrations.AddField(
            model_name='preexistingconditiondatum',
            name='confirmed_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.ConfirmedCase'),
        ),
    ]
