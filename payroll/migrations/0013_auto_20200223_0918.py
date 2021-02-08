# Generated by Django 2.2.1 on 2020-02-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0012_payslip_payment_mothod'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='agent_id',
            field=models.CharField(blank=True, max_length=90, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='payslip',
            name='bank_ac',
            field=models.CharField(blank=True, max_length=90, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='payslip',
            name='bank_name_routing',
            field=models.CharField(blank=True, max_length=9, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='payslip',
            name='personal_no_14_digits',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='payslip',
            name='work_permit_8_digits',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]