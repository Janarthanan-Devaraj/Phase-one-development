from django.contrib import admin

from .models import Notes, Department, Semester

admin.site.register(Notes)
admin.site.register(Department)
admin.site.register(Semester)