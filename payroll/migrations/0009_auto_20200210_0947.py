# Generated by Django 2.2.1 on 2020-02-10 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_auto_20200210_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalpays',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='deductions',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]