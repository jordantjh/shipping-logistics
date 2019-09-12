from django.contrib import admin

from . import models


class ContractAdmin(admin.ModelAdmin):
    list_display = ('num', 'dock_confirmed', 'appointment_confirmed',
                    'delivery_confirmed', 'is_canceled')
    list_editable = ('dock_confirmed', 'appointment_confirmed',
                     'delivery_confirmed', 'is_canceled')


# Register your models here.
admin.site.register(models.Contract, ContractAdmin)
admin.site.register(models.DockConfirmed)
admin.site.register(models.AppointmentConfirmed)
admin.site.register(models.DeliveryConfirmed)
admin.site.register(models.ContractUpdate)
admin.site.register(models.SPNote)
admin.site.register(models.SPContact)
admin.site.register(models.ServiceProvider)
