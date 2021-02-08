from django.urls import path, re_path, reverse
from . import views
from django.contrib import admin

app_name = 'payroll'

urlpatterns = [

path('upload_docs/',views.employee_docs, name='employee_docs'),

path('employee_list',views.EmployeeListView.as_view(),name='employee_list'),
path('table/',views.table,name='table'),

path('employee/<str:pk>/',views.EmployeeDetailView.as_view(),name='employee_detail'),
path('employee_create/',views.EmployeeCreateView.as_view(),name='employee_create'),
path('employee/update/<str:pk>/',views.EmployeeUpdateView.as_view(),name='employee_update'),
path('upload-employee-csv/', views.employee_upload, name="employee_upload"),
path('employee/delete/<str:pk>/',views.EmployeeDeleteView.as_view(),name='employee_delete'),

path('department_create/',views.DepartmentCreateView.as_view(),name='department_create'),
path('department_list',views.DepartmentListView.as_view(),name='department_list'),
path('department/<int:pk>/',views.DepartmentDetailView.as_view(),name='department_detail'),
path('department/update/<int:pk>/',views.DepartmentUpdateView.as_view(),name='department_update'),
path('department/delete/<int:pk>/',views.DepartmentDeleteView.as_view(),name='department_delete'),

path('payslip_list',views.PayslipListView.as_view(),name='payslip_list'),
path('payslip/<int:pk>/',views.PayslipDetailView.as_view(),name='payslip_detail'),
path('payslip_create/',views.PayslipCreateView.as_view(),name='payslip_create'),
path('payslip/update/<int:pk>/',views.PayslipUpdateView.as_view(),name='payslip_update'),
path('upload-payslip-csv/', views.paydetail_upload, name="paydetail_upload"),
path('upload-clinical-csv/', views.clinical_upload, name="clinical_upload"),
path('payslip/delete/<int:pk>/',views.PayslipDeleteView.as_view(),name='payslip_delete'),

path('additional_create/',views.AdditionalCreateView.as_view(),name='additional_create'),
path('additional_list',views.AdditionalListView.as_view(),name='additional_list'),
path('additional/<int:pk>/',views.AdditionalDetailView.as_view(),name='additional_detail'),
path('additional/update/<int:pk>/',views.AdditionalUpdateView.as_view(),name='additional_update'),
path('additional/delete/<int:pk>/',views.AdditionalDeleteView.as_view(),name='additional_delete'),
path('upload-additional_pay-csv/', views.additional_upload, name="additional_upload"),


path('deduction_create/',views.DeductionCreateView.as_view(),name='deduction_create'),
path('deduction_list',views.DeductionListView.as_view(),name='deduction_list'),
path('deduction/<int:pk>/',views.DeductionDetailView.as_view(),name='deduction_detail'),
path('deduction/update/<int:pk>/',views.DeductionUpdateView.as_view(),name='deduction_update'),
path('deduction/delete/<int:pk>/',views.DeductionDeleteView.as_view(),name='deduction_delete'),
path('upload-deduction_pay-csv/', views.deduction_upload, name="deduction_upload"),

path('process_salary/',views.ProcessSalaryListView.as_view(),name='process_salary_list'),
path('payroll_register/',views.PayrollRegisterView.as_view(),name='payroll_register'),
path('process_salary/<int:pk>/',views.ProcessSalaryDetailView.as_view(),name='process_salary_detail'),
path('process_salary_create/',views.ProcessSalaryCreateView.as_view(),name='process_salary_create'),
path('process_salary/update/<int:pk>/',views.ProcessSalaryUpdateView.as_view(),name='process_salary_update'),
path('process_salary/delete/<int:pk>/',views.ProcessSalaryDeleteView.as_view(),name='process_salary_delete'),

path('salary_report/',views.SalaryReport.as_view(),name='salary_report_list'),
path('report_detail/<int:pk>/',views.ReportDetailView.as_view(),name='report_detail'),
path('report_detail_view/<int:pk>/',views.ReportDetailView_Revised.as_view(),name='report_detail_view'),

path('thanks/', views.ThanksPage.as_view(), name="thanks"),

path('employee_payslip/<int:pk>/',views.EmployeePayslip,name='employee_payslip'),
path('salary_process_btn/<int:pk>/',views.update_ps, name='update_ps'),
path('empdeplist/<int:pk>/',views.ListofEmpInDep, name="empdeplist"),

path('payroll_list/',views.ListofPayroll, name="payroll_list"),
path('payroll_detail/<int:pk>/',views.DetailofPayroll, name="payroll_detail"),

path('payroll_report/<slug:payrollid>/<slug:empid>/',views.emppayslip,name='payroll_report'),
path('payroll_report_view/<slug:payrollid>/<slug:empid>',views.emppayslip_view,name='payroll_report_view'),

path('excle/<int:pk>',views.load_workbook, name="excle"),
path('bank_excle/<int:pk>',views.load_workbook_bank, name="bank_excle"),
path('lulu_excle/<int:pk>',views.load_workbook_lulu, name="lulu_excle"),

path ('pdf/<slug:pk>/<slug:empid>', views.payslipPdf, name='pdf'),
path ('pays_detail_pdf/<int:pk>/', views.PaysDetailsPDFView, name='pays_detail_pdf_list'),
path ('pay_detail_list_pdf', views.PayDetailListPDF, name='pay_detail_list_pdf'),
path ('PDFdeduction', views.DeductionsPDFView.as_view(), name='pdf_deduction'),
path ('PDFadditional', views.AdditionalPDFView.as_view(), name='pdf_additional'),

path ('salary_additional/<int:pk>/',views.SalaryAdditional, name="salary_additional"),
path ('salary_deductions/<int:pk>/',views.SalaryDeductions, name="salary_deductions"),
path ('employee_timesheet/<int:pk>/',views.EmpTimesheet, name="emp_timesheet"),

path ('timesheet_list/',views.EmployeeTimesheet.as_view(), name="timesheet_list"),
path('timesheet_create/',views.EmployeeTimesheetCreateView.as_view(),name='timesheet_create'),
path('timesheet/update/<int:pk>/',views.EmployeeTimesheetUpdateView.as_view(),name='timesheet_update'),
path('timesheet/delete/<int:pk>/',views.EmployeeTimesheetDeleteView.as_view(),name='timesheet_delete'),
path('upload-timesheet-csv/', views.timesheet_upload, name="timesheet_upload"),

path ('process_salary_additional/<int:pk>/',views.ProcessSalaryAdditional, name="process_salary_additional"),
path ('process_salary_deductions/<int:pk>/',views.ProcessSalaryDeductions, name="process_salary_deductions"),
path ('process_salary_timesheet/<int:pk>/',views.ProcessSalaryTimesheet, name="process_salary_timesheet"),
path ('process_salary_master/<int:pk>/',views.ProcessSalaryMaster, name="process_salary_master"),
path ('process_salary_paydetails/<int:pk>/',views.ProcessSalaryPayDetails, name="process_salary_paydetails"),
path ('process_salary_bank/<int:pk>/',views.ProcessSalaryBank, name="process_salary_bank"),
path ('process_salary_lulu/<int:pk>/',views.ProcessSalaryLulu, name="process_salary_lulu"),

path ('salary_record/', views.SalaryRecord, name='salary_record'),
path ('salary_record_detail/<slug:empid>', views.SalaryRecordDetail, name='salary_record_detail'),

path('emailpdf/<str:pk>/<str:empid>',views.singleEmail,name='emailpdf'),
path('email/<str:pk>/',views.email,name='email'),
path('downloadAll/<str:pk>/',views.downloadAll,name='downloadAll'),
path('displayPdf/<str:pk>/<str:empid>',views.DisplayPdf.as_view(),name='displayPdf'),

path('delete_all_timesheet/',views.delete_everything, name='delete_everything'),
]
