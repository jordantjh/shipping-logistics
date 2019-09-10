from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Contract)
admin.site.register(models.DockConfirmed)
admin.site.register(models.AppointmentConfirmed)
admin.site.register(models.DeliveryConfirmed)
admin.site.register(models.ContractUpdate)
admin.site.register(models.SPNote)
admin.site.register(models.SPContact)
admin.site.register(models.ServiceProvider)
