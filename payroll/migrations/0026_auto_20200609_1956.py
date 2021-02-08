# Generated by Django 2.2.1 on 2020-06-09 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0025_clinical'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinical',
            name='competencies',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinical',
            name='date_qualified',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='doh_licence_as',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='healthy_fit',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinical',
            name='higest_qualification',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='licence_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='non_doh_licence_no',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='previous_visa_sponser',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='visa_status',
            field=models.CharField(choices=[('Employer with NOC', 'Employer with NOC'), ('Visit/Tourist', 'Visit/Tourist'), ('Cancelled', 'Cancelled'), ('Spouse/Parent', 'Spouse/Parent')], default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clinical',
            name='work_order',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
    ]
