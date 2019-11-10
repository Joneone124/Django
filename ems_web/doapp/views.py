import os
import uuid

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from adminapp.models import Emp


def emplist(request):
    if request.session.get('login'):
        number = request.GET.get('page')
        print(number)
        if number is None:
            number = 1
        emp = Emp.objects.all()
        pagntor = Paginator(emp, per_page=3)
        pg = pagntor.page(number)
        return render(request, 'doapp/emplist.html', {'page': pg})
    else:
        return redirect('adminapp:login')

def addemp(request):
    if request.session.get('login'):
        # return redirect('doapp:emplist')
        print('lllll')
        return render(request, 'doapp/addEmp.html')
    else:
        return redirect('adminapp:login')

def addempdo(request):
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    head = request.FILES.get('head')

    rst = str(uuid.uuid4()) + os.path.splitext(head.name)[1]
    head.name = rst
    print(name, salary, age, head)
    Emp.objects.create(name = name, salary = salary, age = age, head = head)
    return redirect('doapp:emplist')

def deleteemp(request):
    id = request.GET.get('id')
    # print(id)
    # name = request.GET.get('name')
    Emp.objects.get(id = id).delete()
    return redirect('doapp:emplist')

def updateemp(request):
    id = request.GET.get('id')
    return render(request,'doapp/updateEmp.html',{'id':id})

def updateempdo(request):
    id = request.GET.get('id')
    name = request.POST.get('name')
    salary = request.POST.get('salary')
    age = request.POST.get('age')
    head = request.FILES.get('head')

    rst = str(uuid.uuid4()) + os.path.splitext(head.name)[1]
    head.name = rst
    print(name, salary, age, head)
    emp = Emp.objects.get(id = id)
    emp.name = name
    emp.age = age
    emp.salary = salary
    emp.head = head
    emp.save()
    return redirect('doapp:emplist')