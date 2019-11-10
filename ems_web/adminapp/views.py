import random
import string

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from adminapp.captcha.image import ImageCaptcha
from adminapp.models import Admin


def regist(request):
    return render(request,"adminapp/regist.html")

def registdo(request):
    username = request.POST.get('username')
    name = request.POST.get('name')
    password = request.POST.get('pwd')
    sex = request.POST.get('sex')
    if sex == 'true':
        sex = True
    else:
        sex = False
    number = request.POST.get('number')
    print(username,name,password,sex,number)
    code = request.session['code']
    if number.lower() == code.lower():
        Admin.objects.create(username=username,name=name,password=password,sex=sex)
        return redirect("adminapp:login")
    else:
        return redirect("adminapp:regist")

def getcaptcha(request):
    img = ImageCaptcha()
    rst = random.sample(string.ascii_letters+string.digits,5)
    print(rst)
    code = ''.join(rst)
    print(code)
    request.session['code'] = code
    data = img.generate(code)
    return HttpResponse(data,'image/png')

def login(request):
    if request.COOKIES.get('password') and  request.COOKIES.get('username'):
        request.session['login'] = 'login'
        print('jjjjjjjjjjjjjjjjjjjjjjjjjjj')
        return redirect('doapp:emplist')
    else:
        return render(request,"adminapp/login.html")
    # if request.COOKIES['password'] == Admin.objects.get(username=request.COOKIES['username']).password:
    #     return redirect('doapp:emplist')
    # return render(request,"adminapp/login.html")

def logindo(request):
    name = request.POST.get('name')
    password = request.POST.get('pwd')
    if Admin.objects.get(username=name).password == password:
        request.session['login'] = 'login'
        red = redirect('doapp:emplist')
        red.set_cookie("username",name)
        red.set_cookie("password",password)
        return red
    else:
        return redirect('adminapp:login')
