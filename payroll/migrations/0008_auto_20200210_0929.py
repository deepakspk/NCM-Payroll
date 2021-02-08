# Generated by Django 2.2.1 on 2020-02-10 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0007_auto_20200210_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='cost_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department_name', to='payroll.CostCenter'),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='work_permit',
            field=models.CharField(choices=[('Uniteam', 'Uniteam'), ('Aspen', 'Aspen'), ('Uniteam(Br2)', 'Uniteam(Br2)')], max_length=60),
        ),
        migrations.AlterField(
            model_name='report',
            name='work_permit',
            field=models.CharField(choices=[('Uniteam', 'Uniteam'), ('Aspen', 'Aspen'), ('Uniteam(Br2)', 'Uniteam(Br2)')], default=0, max_length=60),
            preserve_default=False,
        ),
    ]
