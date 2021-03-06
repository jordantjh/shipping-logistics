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
    latest_update = models.CharField(max_length=100, blank=True, null=True)
    is_canceled = models.BooleanField(default=False)

    def __str__(self):
        return self.num


class ContractUpdate(models.Model):
    contract_id = models.ForeignKey('Contract', on_delete=models.CASCADE)
    author = models.CharField(max_length=25)
    event_name = models.CharField(max_length=100)
    event_time = models.DateTimeField(blank=True, null=True)
    time_added = models.DateTimeField(
        default=datetime.now, blank=True, null=True)


class AppointmentConfirmed(models.Model):
    contract_id = models.ForeignKey('Contract', on_delete=models.CASCADE)
    appt_date = models.DateTimeField(blank=True, null=True)
    appt_by_user = models.CharField(max_length=25)

    comment = models.TextField(blank=True, null=True)
    time_added = models.DateTimeField(
        default=datetime.now, blank=True, null=True)


class DockConfirmed(models.Model):
    contract_id = models.ForeignKey('Contract', on_delete=models.CASCADE)
    delivery_datetime = models.DateTimeField(blank=True, null=True)
    signed_by = models.CharField(max_length=25)
    condition_comment = models.CharField(max_length=50)
    time_added = models.DateTimeField(
        default=datetime.now, blank=True, null=True)


class DeliveryConfirmed(models.Model):
    contract_id = models.ForeignKey('Contract', on_delete=models.CASCADE)
    delivery_datetime = models.DateTimeField(blank=True, null=True)
    signed_by = models.CharField(max_length=25)
    condition_comment = models.CharField(max_length=50)
    signed_pod = models.ImageField(upload_to='pods/')
    time_added = models.DateTimeField(
        default=datetime.now, blank=True, null=True)


class ServiceProvider(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)


class SPNote(models.Model):
    content = models.CharField(max_length=30)
    author = models.CharField(max_length=30)


class SPContact(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    off_phone = models.CharField(max_length=30)
    off_ex = models.CharField(max_length=4)
    fax = models.CharField(max_length=10)
    addr = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
