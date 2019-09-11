from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Contract)
admin.site.register(models.SPNote)
admin.site.register(models.SPContact)
admin.site.register(models.ServiceProvider)