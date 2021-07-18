from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('FullName','MobileNo','EmpCode','Designation')
        labels = {
            'Designation' : 'Position'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['Designation'].empty_label = "Select"
        self.fields['EmpCode'].required = False

