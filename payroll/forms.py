from .models import Department, Employee, Payslip, ProcessSalary, Additionalpay, Deduction, Timesheet, Document, Leave
from django.forms import ModelForm, Form
from django import forms
from . import models

class DepartmentForm(ModelForm):
    class Meta:
        model= Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class EmployeeForm(ModelForm):
    class Meta:
        model= Employee
        fields = '__all__'
        exclude = ('employee_status',)
        unique_together = [("first_name", "last_name" )]
        widgets = {
            'DOB':forms.DateInput(attrs={'type':'date'}),
            'joining_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class DocumentForm(ModelForm):
    class Meta:
        model= Document
        fields = '__all__'

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class LeaveForm(ModelForm):
    class Meta:
        model= Leave
        fields = '__all__'
        widgets = {
            'date_from':forms.DateInput(attrs={'type':'date'}),
            'date_to':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})
        

class AdditionalForm(ModelForm):
    class Meta:
        model= Additionalpay
        fields = '__all__'
        widgets = {
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'})
        }


    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class DeductionForm(ModelForm):
    class Meta:
        model= Deduction
        fields = '__all__'
        widgets = {
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})

class TimesheetForm(ModelForm):
    class Meta:
        model= Timesheet
        fields = '__all__'
        widgets = {
            'month':forms.DateInput(attrs={'type':'date'}),
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'end_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})



class PayslipForm(ModelForm):
    class Meta:
        model= Payslip
        fields = '__all__'
        widgets = {
            'joining_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         data = models.Payslip.objects.all().values_list('employee',flat=True)
         # self.fields['employee'].queryset = models.Employee.objects.exclude(employee_id__in=data)
         self.fields['employee'].queryset = models.Employee.objects.exclude(employee_status = 'Inactive')
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})


class ProcessSalaryForm(ModelForm):
    class Meta:
        model= ProcessSalary
        fields = '__all__'
        exclude = ('status','gross_pay','Additional_pay','deduction','total', 'employee_count', 'actual_gross_pay')
        widgets = {
            'salary_month':forms.DateInput(attrs={'type':'date'}),
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'finish_date':forms.DateInput(attrs={'type':'date'})
        }

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         for field in self.fields:
             self.fields[field].widget.attrs.update({'class':'form-control'})
