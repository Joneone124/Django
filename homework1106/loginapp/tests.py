from django.test import TestCase
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "homework1106.settings")
django.setup()
from loginapp.models import User,Employee,Department
# Create your tests here.

# user1 = User.objects.create(name="xiaoming",password="11111")
# user2 = User.objects.create(name="xiaoming",password="1024")
# user3 = User.objects.create(name="xiaoming",password="8848")
# user2 = User.objects.create(name="xiaozhang",password="123456")
# user3 = User.objects.create(name="xiaoli",password="123456")

# emp1 = Employee.objects.create(name="xiaoliu",password="123456")
# emp2 = Employee.objects.create(name="xiaoguo",password="123456")
# emp3 = Employee.objects.create(name="xiaozhou",password="123456")

# dep1 = Department.objects.create(name="bumen1")
# dep2 = Department.objects.create(name="bumen2")
# dep3 = Department.objects.create(name="bumen3")