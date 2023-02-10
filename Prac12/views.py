from datetime import datetime
from django.shortcuts import render, redirect
from Prac12.forms import EmployeeForm
from django.contrib import messages
from Prac12.models import Employee


def emp_create(request):
    if request.method != 'POST':
        newForm = EmployeeForm(initial={'empid':'auto'})
        return render(request, 'emp_create.html', {'form':newForm})
    else:
        newEmpID = genNewEmpID()
        request.POST._mutable = True
        request.POST['empid'] = newEmpID
        request.POST._mutable = False
        newForm = EmployeeForm(request.POST)
        if newForm.is_valid():
            newForm.save()
            messages.success(request, "New employee data saved...")
        return redirect('home')

def genNewEmpID():
    currentYear = str(datetime.date.today().year)
    lastEmployee = Employee.objects.last()
    if lastEmployee:
        lastID = lastEmployee.empid
        lastID = lastID[8:]
        newID = int(lastID) + 1
        newID = str(newID)
        addZero = 5-len(newID)
        newID = ("0" * addZero) + newID
        return "Emp" + currentYear + "-" + newID
    else:
        return "Emp" + currentYear + "-" + "00001"