from django.contrib import admin

from .models import User, AcademicsInfo, CompanyInfo

admin.site.register(User)
admin.site.register(AcademicsInfo)
admin.site.register(CompanyInfo)
