from django.contrib import admin
from .models import Department
from .models import Employee
from .models import Payslip, Timesheet, ReportTimesheet
from .models import ProcessSalary, Additionalpay, Deduction, Report, Additionalpays, Deductions,AdditionalPaysAdmin, CostCenter, Clinical
# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Payslip)
admin.site.register(ProcessSalary)
admin.site.register(Additionalpay)
admin.site.register(Deduction)
admin.site.register(Report)
admin.site.register(Additionalpays,AdditionalPaysAdmin)
admin.site.register(Deductions)
admin.site.register(CostCenter)
admin.site.register(Timesheet)
admin.site.register(ReportTimesheet)
admin.site.register(Clinical)