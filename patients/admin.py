from django.contrib import admin
from django.contrib.auth.models import Group
from .models import PatientDemo

# Register your models here.
admin.site.register(PatientDemo)
admin.site.unregister(Group)
admin.site.site_header = "Patient Manager Admin View"
