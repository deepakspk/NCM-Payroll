# Generated by Django 2.2.1 on 2020-02-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_auto_20200205_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='work_permit',
        ),
        migrations.AddField(
            model_name='payslip',
            name='work_permit',
            field=models.CharField(choices=[('Uniteam', 'Uniteam'), ('Aspen', 'Aspen'), ('Uniteam(Br2)', 'Uniteam(Br2)')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
