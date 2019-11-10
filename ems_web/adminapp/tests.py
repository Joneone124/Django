from django.test import TestCase
import os,django

from adminapp.models import Admin

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ems_web.settings")
django.setup()

# Create your tests here.
# Admin.objects.create(name = 'user1', realname = 'xiaoming', sex = True)