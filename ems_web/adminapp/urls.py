from django.urls import path, include
import adminapp.views as views

app_name = 'adminapp'
urlpatterns = [
    path('regist/',views.regist, name = 'regist'),
    path('registdo/',views.registdo, name = 'registdo'),
    path('getcaptcha/',views.getcaptcha, name = 'getcaptcha'),
    path('login/',views.login, name = 'login'),
    path('logindo/',views.logindo, name = 'logindo'),
]