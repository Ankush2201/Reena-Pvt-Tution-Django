from django.contrib import admin
from firstapp.models import *
from firstapp.forms import *

# Register your models here.
admin.site.register(Student)
# admin.site.register(LoginForm)
admin.site.register(Contact)

