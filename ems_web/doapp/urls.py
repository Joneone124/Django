from django.urls import path
import doapp.views as views
app_name = 'doapp'
urlpatterns = [
    path('emplist/',views.emplist, name = 'emplist'),
    path('addemp/',views.addemp, name = 'addemp'),
    path('addempdo/',views.addempdo, name = 'addempdo'),
    path('deleteemp/',views.deleteemp, name = 'deleteemp'),
    path('updateemp/',views.updateemp, name = 'updateemp'),
    path('updateempdo/',views.updateempdo, name = 'updateempdo'),
]