# Generated by Django 2.2.1 on 2020-03-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0019_reporttimesheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='processsalary',
            name='actual_gross_pay',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]