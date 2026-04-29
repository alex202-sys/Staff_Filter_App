from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben
    print('Das funktioniert gut!')
    employees = Employee.objects.all()
    # print(employees)

    employees3000 = Employee.objects.filter(
        Q(salary__gt=3000)).order_by('name')
    # print(employees3000)

    anzahl = Employee.objects.filter(salary__gte=5000).count()
    print(anzahl)
    
    durchgehalt = Employee.objects.filter(department__name='Sales').aggregate(Avg('salary'))
    # durchgehalt = round(durchgehalt['salary__avg'], 2)
    durchgehalt = round(durchgehalt['salary__avg'], 2)
    print(durchgehalt)

    employeese2022NotHR = Employee.objects.filter(Q(hire_date__lt=date(2022, 1, 1)) & ~Q(department__name='HR'))
    print(employeese2022NotHR) 

    #     employees3000 = Employee.objects.filter(
    #     Q(salary__gt=5000) | Q(department__name='IT'),
    #     hire_date__year__gt=2015
    # ).order_by('name')

    return render(request, 'employee_list.html', {'employee_list' : employees, 'employees3000' : employees3000, 'employeesCount5000' : anzahl, 'durchgehalt' : durchgehalt, 'employeesBefore2022NotHR' : employeese2022NotHR})