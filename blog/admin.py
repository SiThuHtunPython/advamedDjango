from django.contrib import admin
from .models import Maintenance, ServiceRecord, InstallationRecord

admin.site.register(Maintenance)
admin.site.register(ServiceRecord)
admin.site.register(InstallationRecord)
