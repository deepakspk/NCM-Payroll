# Generated by Django 2.2.1 on 2021-02-20 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0035_auto_20210220_1944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='mode_of_payment',
        ),
        migrations.AlterField(
            model_name='payslip',
            name='payment_method',
            field=models.CharField(choices=[('Bank', 'Bank'), ('Cash', 'Cash'), ('Other', 'Other')], max_length=15),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='work_permit',
            field=models.CharField(choices=[('Nepal Can Move', 'Nepal Can Move'), ('Nepal Can Buy', 'Nepal Can Buy'), ('Nepal Can Code', 'Nepal Can Code')], max_length=60),
        ),
    ]
