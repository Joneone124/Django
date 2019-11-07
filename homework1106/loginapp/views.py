from django.http import HttpResponse
from django.shortcuts import render
from loginapp.models import User,Employee,Department
# Create your views here.

def login(request):
    return render(request,"login.html")

def logincheck(request):
    name = request.POST.get("username")
    biao = request.POST.get("biao")
    print(name,biao)
    if biao == "yonghu":
        qs_yonghu = User.objects.filter(name=name)
        return render(request, "sub1.html", {"qs_yonghu": qs_yonghu}, {"q_length": len(qs_yonghu)})
    if biao == "yuangong":
        qs_yonghu = Employee.objects.filter(name=name)
        return render(request, "sub2.html", {"qs_yuangong": qs_yonghu}, {"q_length": len(qs_yonghu)})
    if biao == "bumen":
        qs_yonghu = Department.objects.filter(name=name)
        return render(request, "sub3.html", {"qs_bumen": qs_yonghu}, {"q_length": len(qs_yonghu)})