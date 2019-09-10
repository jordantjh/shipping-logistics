from django.db import models
from datetime import datetime

# Create your models here.


class Contract(models.Model):
    num = models.CharField(max_length=30)
    terminal = models.CharField(max_length=25)
    service = models.CharField(max_length=15)  # "First Mile" or "Final Mile"
    service_type = models.CharField(max_length=25)  # "signature plus"
    service_provider = models.CharField(max_length=80)
    consignee_name = models.CharField(max_length=35)
    # blank is for admin, null for db
    eta_dock = models.DateTimeField(blank=True, null=True)
    dock_confirmed = models.BooleanField(default=False)
    appointment_confirmed = models.BooleanField(default=False)
    delivery_confirmed = models.BooleanField(default=False)
    time_added = models.DateTimeField(default=datetime.now)
    deadline = models.DateTimeField(blank=True, null=True)
    account_id_num = models.CharField(max_length=25)
    account_name = models.CharField(max_length=25)
    account_ref_num = models.CharField(max_length=20)
    booker_name = models.CharField(max_length=35)
    status = models.CharField(max_length=20)
