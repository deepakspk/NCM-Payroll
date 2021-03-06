from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from django.contrib import admin


# Create your models here.

class Department(models.Model):
    department = models.CharField(unique=True, max_length=40)
    def __str__(self):
        return self.department

class CostCenter(models.Model):
    cost_center = models.CharField(unique=True, max_length=40)
    def __str__(self):
        return self.cost_center

class NepaliDate(models.Model):
    year                   =   models.CharField(max_length=60,)
    month                  =   models.CharField(max_length=60,)
    start                  =   models.DateField()
    end                    =   models.DateField()
    days                   =   models.DecimalField(max_digits=12, decimal_places=2,)   

    def __str__(self):
        return str(self.month) +'__'+ str(self.year)

class Employee(models.Model):
    employee_id         = models.CharField(primary_key=True, max_length=60, unique=True)
    first_name          = models.CharField(max_length=60, blank=True,null=True)
    middle_name         = models.CharField(max_length=60, blank=True,null=True)
    last_name           = models.CharField(max_length=60, blank=True,null=True)
    GENDER_CHOICES      = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'),)
    gender              = models.CharField(max_length=10, choices=GENDER_CHOICES)
    DOB                 = models.DateField(null=True, blank=True)
    religion            = models.CharField(max_length=20, null=True, blank=True)
    citizenship         = models.CharField(max_length=20, null=True, blank=True)
    email               = models.EmailField(max_length=70, blank=True,null=True)
    phone               = models.IntegerField(null=True, blank=True,default=0)
    current_address     = models.CharField(max_length=90, null=True, blank=True)
    permanent_address   = models.CharField(max_length=90, null=True, blank=True)
    department          = models.ForeignKey(Department, related_name='dept_name', on_delete=models.CASCADE,null=True,blank=True)
    designation         = models.CharField(max_length=40, null=True, blank=True)
    department_head     = models.BooleanField(default=False)
    joining_date        = models.DateField(null=True, blank=True)
    img                 = models.ImageField(upload_to='pics',null=True,blank=True, default='/static/images/default-user.jpg')
    employee_status_choice     = (('Active', 'Active'),('Inactive', 'Inactive'))
    employee_status            = models.CharField(max_length=10, default=['Active'], choices=employee_status_choice)

    def __str__ (self):
        return str(self.first_name)+' '+ str(self.last_name)

    def get_absolute_url(self):
         return reverse("payroll:employee_detail", kwargs={'pk':self.pk})

    @property
    def full_name(self):
        return str(self.first_name) +" "+ str(self.last_name)

class Document(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_document', on_delete=models.CASCADE, blank=True,null=True) 
    category_choices       = (('ID', 'ID'),
                            ('Personal', 'Personal'),
                            ('Employment', 'Employment'),
                            ('Letter', 'Letter'),
                            ('Other', 'Other'),)
    category              =   models.CharField(max_length=60, choices=category_choices, blank=True,null=True)
    label                 =   models.CharField(max_length=160, blank=True,null=True)
    document              =   models.FileField(upload_to='documents/')

def __str__(self):
    return str(self.employee)

class Leave(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_leave', on_delete=models.CASCADE, blank=True,null=True) 
    leave_choices       = (('Annual', 'Annual'),
                            ('Sick', 'Sick'),
                            ('LWOP', 'LWOP'),
                            ('Special', 'Special'),)
    leave              =   models.CharField(max_length=60, choices=leave_choices, blank=True,null=True)
    date_from          =   models.DateField(null=True, blank=True)
    date_to            =   models.DateField(null=True, blank=True)
    approve_by         =   models.ForeignKey(Employee, related_name='approve_by', on_delete=models.CASCADE, blank=True,null=True) 
    comment            =   models.TextField(max_length=260, blank=True,null=True)


def __str__(self):
    return str(self.employee)

class Payslip(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_payslip', on_delete=models.CASCADE, blank=True,null=True)
    basic_salary           =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    housing_allowance      =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    transportation_allowance = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    other                  =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    work_permit_choice     =   (('Nepal Can Move', 'Nepal Can Move'),('Nepal Can Buy', 'Nepal Can Buy'),('Nepal Can Code', 'Nepal Can Code'),)
    work_permit            =   models.CharField(max_length=60, choices=work_permit_choice)
    cost_center            =   models.ForeignKey(CostCenter, related_name='dept_name', on_delete=models.CASCADE,null=True,blank=True)
    PAYMENT_METHOD_CHOICES = (('Bank', 'Bank'),('Cash', 'Cash'),('Other','Other'),)
    payment_method         =   models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES)
    bank_name              =   models.CharField(max_length=9, blank=True,null=True,)
    bank_ac                =   models.CharField(max_length=90, blank=True,null=True,)    
    
    
    def __str__ (self):
        return str(self.employee)

    @property
    def gross_pay(self):
        return self.basic_salary + self.housing_allowance + self.transportation_allowance + self.other

class Clinical(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_clinical', on_delete=models.CASCADE, blank=True,null=True)
    seha_id                =   models.CharField(max_length=90, blank=True,null=True,)
    zoho_id                =   models.CharField(max_length=90, blank=True,null=True,)
    company_email          =   models.EmailField(max_length=70, blank=True,null=True)
    source                 =   models.CharField(max_length=90, blank=True,null=True,)
    source_entity          =   models.CharField(max_length=90, blank=True,null=True,)
    category               =   models.CharField(max_length=90, blank=True,null=True,)
    hiring_status          =   models.CharField(max_length=90, blank=True,null=True,)
    emirates_id            =   models.CharField(max_length=90, blank=True,null=True,)
    Passport_no            =   models.CharField(max_length=90, blank=True,null=True,)
    passport_expiry        =   models.DateField(null=True, blank=True)
    licence_authority      =   models.CharField(max_length=90, blank=True,null=True,)
    doh_licence            =   models.CharField(max_length=90, blank=True,null=True,)
    doh_licence_type_choices = (('Permanent', 'Permanent'),('Temporary', 'Temporary'),)
    doh_licence_type       =   models.CharField(max_length=15, choices=doh_licence_type_choices)
    doh_licence_no         =   models.CharField(max_length=90, blank=True,null=True,)
    previous_company       =   models.CharField(max_length=90, blank=True,null=True,)
    licence_issued_date    =   models.DateField(null=True, blank=True)
    licence_issued_date    =   models.DateField(null=True, blank=True)
    licence_expiry_date    =   models.DateField(null=True, blank=True)
    non_doh_licence_no     =   models.CharField(max_length=90, blank=True,null=True,)
    higest_qualification   =   models.CharField(max_length=90, blank=True,null=True,)
    date_qualified         =   models.DateField(null=True, blank=True)
    clinic_exp_in_5_year_c =   (('TRUE', 'TRUE'),('FALSE', 'FALSE'),)
    clinic_exp_in_5_year   =   models.CharField(max_length=15, choices=clinic_exp_in_5_year_c)
    healthy_fit_c          =   (('TRUE', 'TRUE'),('False', 'FALSE'),)
    healthy_fit            =   models.CharField(max_length=15, choices=healthy_fit_c)
    competencies_c         =   (('TRUE', 'TRUE'),('FALSE', 'FALSE'),)
    competencies           =   models.CharField(max_length=15, choices=competencies_c)
    visa_status_c         =   (('Employer with NOC', 'Employer with NOC'),('Visit/Tourist', 'Visit/Tourist'),('Cancelled', 'Cancelled'),('Spouse/Parent', 'Spouse/Parent'),)
    visa_status           =   models.CharField(max_length=90, choices=visa_status_c)
    previous_visa_sponser =   models.CharField(max_length=90, blank=True,null=True,)
    doh_licence_as        =   models.CharField(max_length=90, blank=True,null=True,)
    work_order            =   models.CharField(max_length=90, blank=True,null=True,)

    def __str__ (self):
        return str(self.employee)


class Timesheet(models.Model):
    employee               =   models.ForeignKey(Employee, related_name='employee_timesheet', on_delete=models.CASCADE, blank=True,null=True)
    month                  =   models.ForeignKey(NepaliDate, related_name='nepali_date', on_delete=models.CASCADE, blank=True,null=True)
    partial_choice         =   (('N', 'N'),('Y', 'Y'))
    partial                =   models.CharField(max_length=60, choices=partial_choice,)
    # hours                  =   models.DecimalField(max_digits=12, decimal_places=2,)
    normal                 =   models.DecimalField(max_digits=12, decimal_places=2,)
    weekend                =   models.DecimalField(max_digits=12, decimal_places=2,)
    holiday                =   models.DecimalField(max_digits=12, decimal_places=2,)
    vacation               =   models.DecimalField(max_digits=12, decimal_places=2,)
    sick                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    lwop                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    # total                  =   models.DecimalField(max_digits=12, decimal_places=2,)

    def __str__(self):
        return str(self.employee) +'__'+ str(self.month)

    @property
    def month_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick + self.lwop

    @property
    def pay_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick


class Additionalpay(models.Model):
    payslip               =   models.ForeignKey(Payslip, related_name='additional_pay', on_delete=models.CASCADE,blank=True,null=True)
    month                  =   models.ForeignKey(NepaliDate, related_name='nepali_date_additional', on_delete=models.CASCADE, blank=True,null=True)
    ADDITIONALPAY_CHOICES  = (('Expense Reimbursement', 'Expense Reimbursement'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Bonus', 'Bonus'),
                              ('Overtime/ Holiday Pay', 'Overtime/ Holiday Pay'),
                              ('Other', 'Other'),)
    additional             =   models.CharField(max_length=60, choices=ADDITIONALPAY_CHOICES, blank=True,null=True)
    additional_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                 =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    # OCCURS_CHOICE          = (('Once', 'Once'),
                            # ('Monthly', 'Monthly'),)
    # occur                  =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    # start_date             =   models.DateField(null=True, blank=True)
    # end_date               =   models.DateField(null=True, blank=True)


    def __str__ (self):
        return str(self.additional)

class Deduction(models.Model):
    payslip               =   models.ForeignKey(Payslip, related_name='salary_deduction', on_delete=models.CASCADE,blank=True,null=True)
    month                 =   models.ForeignKey(NepaliDate, related_name='nepali_date_deduction', on_delete=models.CASCADE, blank=True,null=True)
    DEDUCTION_CHOICES     =   (('Housing Loan', 'Housing Loan'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Traffic Fine', 'Traffic Fine'),
                              ('Loan', 'Loan'),
                              ('Unpaid sick leave', 'Unpaid sick leave'),
                              ('Other', 'Other'),)
    deduction             =   models.CharField(max_length=60, choices=DEDUCTION_CHOICES, blank=True,null=True)
    deduction_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE         = (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    # occur                  =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    # start_date             =   models.DateField(null=True, blank=True)
    # end_date               =   models.DateField(null=True, blank=True)


    def __str__ (self):
        return str(self.deduction)


class ProcessSalary(models.Model):
    payroll_id      = models.CharField(max_length=90, blank=True,null=True)
    salary_month    = models.ForeignKey(NepaliDate, related_name='nepali_date_ps', on_delete=models.CASCADE, blank=True,null=True)
    employee        = models.ManyToManyField(Payslip, related_name='employee_name')
    SALARY_TYPES    = (('Normal', 'Normal'),
                      ('Adjustment', 'Adjustment'),)
    salary_type     = models.CharField(max_length=60, default=SALARY_TYPES[0][0], choices=SALARY_TYPES, blank=True,null=True)
    SALARY_STATUS   = (('Processing', 'Processing'),
                      ('Processed', 'Processed'),
                      ('Paid', 'Paid'),)
    status          = models.CharField(max_length=60, default=SALARY_STATUS[0][0], choices=SALARY_STATUS, blank=True,null=True)
    employee_count  = models.IntegerField(null=True, blank=True,default=0)
    gross_pay       = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    actual_gross_pay= models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    Additional_pay  = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    deduction       = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    total           = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)

    def __str__(self):
        return str(self.payroll_id)

    def get_absolute_url(self):
        return reverse("payroll:process_salary_detail", kwargs={'pk':self.pk})

    @property
    def actual_payroll_id(self):
        return "UMA" + str(self.id)

class Report(models.Model):
    employee_id         = models.CharField(max_length=60)
    first_name          = models.CharField(max_length=60, blank=True,null=True)
    last_name           = models.CharField(max_length=60, blank=True,null=True)
    department          = models.CharField(max_length=60, blank=True,null=True)
    designation         = models.CharField(max_length=40, null=True, blank=True)
    work_permit_choice  = (('Nepal Can Move', 'Nepal Can Move'),('Nepal Can Buy', 'Nepal Can Buy'),('Nepal Can Code', 'Nepal Can Code'),)
    work_permit         = models.CharField(max_length=60, choices=work_permit_choice)
    cost_center         = models.ForeignKey(CostCenter, related_name='department_name', on_delete=models.CASCADE,null=True,blank=True)
    payroll_id          = models.CharField(max_length=90, blank=True,null=True)
    payroll_month       = models.ForeignKey(NepaliDate, related_name='nepali_date_report', on_delete=models.CASCADE, blank=True,null=True)
    PAYMENT_METHOD_CHOICES = (('Bank', 'Bank'),('Cash', 'Cash'),('Other','Other'),)
    payment_method         =   models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES)
    bank_name              =   models.CharField(max_length=9, blank=True,null=True,)
    bank_ac                =   models.CharField(max_length=90, blank=True,null=True,)    
    
    basic_salary        = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    housing_allowance   = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    transportation_allowance = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    other               = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    lowp_deduction      = models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)

    def __str__(self):
        return str(self.employee_id) +'__'+ str(self.payroll_id)

    def get_absolute_url(self):
        return reverse("payroll:salary_report", kwargs={'pk':self.pk})

    @property
    def full_name(self):
        return str(self.first_name) +" "+ str(self.last_name)

    @property
    def gross_pay(self):
        others = self.other or 0
        return self.basic_salary + self.housing_allowance + self.transportation_allowance + others

class Additionalpays(models.Model):
    ADDITIONALPAY_CHOICES  = (('Annual Air Ticket', 'Annual Air Ticket'),
                              ('Expense Reimbursement', 'Expense Reimbursement'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Bonus', 'Bonus'),
                              ('Overtime/ Holiday Pay', 'Overtime/ Holiday Pay'),
                              ('Other', 'Other'),)
    report                 = models.ForeignKey(Report, on_delete=models.CASCADE)
    month                  = models.ForeignKey(NepaliDate, related_name='nepali_date_add', on_delete=models.CASCADE, blank=True,null=True)
    additional             =   models.CharField(max_length=60, choices=ADDITIONALPAY_CHOICES, blank=True,null=True)
    additional_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                 =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE          = (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    # occur                  =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    # start_date             =   models.DateField(null=True, blank=True)
    # end_date               =   models.DateField(null=True, blank=True)


    def __str__ (self):
        return str(self.additional)

class AdditionalPaysAdmin(admin.ModelAdmin):
    list_display = ('report','additional')

class Deductions(models.Model):
    DEDUCTION_CHOICES     =   (('Housing Loan', 'Housing Loan'),
                              ('Salary Advance', 'Salary Advance'),
                              ('Traffic Fine', 'Traffic Fine'),
                              ('Loan', 'Loan'),
                              ('Other', 'Other'),)
    report                =   models.ForeignKey(Report, on_delete=models.CASCADE)
    month                 =   models.ForeignKey(NepaliDate, related_name='nepali_date_ded', on_delete=models.CASCADE, blank=True,null=True)
    deduction             =   models.CharField(max_length=90, blank=True,null=True)
    deduction_label       =   models.CharField(max_length=90, blank=True,null=True)
    amount                =   models.DecimalField(max_digits=12, decimal_places=2, blank=True,null=True)
    OCCURS_CHOICE         =  (('Once', 'Once'),
                             ('Monthly', 'Monthly'),)
    # occur                 =   models.CharField(max_length=60, choices=OCCURS_CHOICE, blank=True,null=True)
    # start_date            =   models.DateField(null=True, blank=True)
    # end_date              =   models.DateField(null=True, blank=True)

    def __str__ (self):
        return str(self.deduction)


class ReportTimesheet(models.Model):
    report                 =   models.ForeignKey(Report, on_delete=models.CASCADE)
    employee               =   models.CharField(max_length=60,)
    month                  =   models.ForeignKey(NepaliDate, related_name='nepali_date_rt', on_delete=models.CASCADE, blank=True,null=True)
    partial                =   models.CharField(max_length=60,)
    normal                 =   models.DecimalField(max_digits=12, decimal_places=2,)
    weekend                =   models.DecimalField(max_digits=12, decimal_places=2,)
    holiday                =   models.DecimalField(max_digits=12, decimal_places=2,)
    vacation               =   models.DecimalField(max_digits=12, decimal_places=2,)
    sick                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    lwop                   =   models.DecimalField(max_digits=12, decimal_places=2,)
    total                  =   models.DecimalField(max_digits=12, decimal_places=2,)

    def __str__(self):
        return str(self.employee) +'__'+ str(self.month)

    @property
    def month_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick + self.lwop

    @property
    def pay_days(self):
        return self.normal + self.weekend + self.holiday + self.vacation+ self.sick

class ReportNepaliDate(models.Model):
    year                   =   models.CharField(max_length=60,)
    month                  =   models.CharField(max_length=60,)
    start                  =   models.DateField()
    end                    =   models.DateField()
    days                   =   models.DecimalField(max_digits=12, decimal_places=2,)   

    def __str__(self):
        return str(self.month) +'__'+ str(self.year)
