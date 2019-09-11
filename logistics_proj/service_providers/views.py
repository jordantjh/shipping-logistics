from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

from .models import Contract, ContractUpdate

# Create your views here.


def contractsView(req):
    filter_by_param = req.GET.get('filterby', '')  # '' if not found
    if filter_by_param == 'dock-confirmed':
        contracts = Contract.objects.filter(dock_confirmed=True)
    elif filter_by_param == 'appointment-confirmed':
        contracts = Contract.objects.filter(appointment_confirmed=True)
    elif filter_by_param == 'delivery-confirmed':
        contracts = Contract.objects.filter(delivery_confirmed=True)
    elif filter_by_param == 'canceled':
        contracts = Contract.objects.filter(is_canceled=True)
    else:
        contracts = Contract.objects.all()
    return render(req, 'contracts.html', {'contracts': contracts})


def contractsDetailsView(req, contract_id):
    if req.method == "GET":
        contract = Contract.objects.get(id=contract_id)
        return render(req, 'contracts_details.html', {'contract': contract})

    ### POST request ###
    # Grab data from form
    event_name = req.POST['update-event']
    event_time_raw = req.POST['update-datetime']
    event_time_datetime = datetime.strptime(
        event_time_raw, "%Y/%m/%d %H:%M").date()

    if event_name == 'dock-confirmed':
        signed_by = req.POST['signed_by']
        condition_comment = req.POST['condition_comment']

    elif event_name == 'appt-confirmed':
        appt_by_user = req.POST['appt_by_user']
        appt_comment = req.POST['appt_comment']

    elif event_name == 'delivery-confirmed':
        signed_by = req.POST['signed_by']
        condition_comment = req.POST['condition_comment']
        pod_upload = req.POST['pod_upload']

    messages.success(
        req, 'Update has been successfully added.', extra_tags='text-success')
    contract = Contract.objects.get(id=contract_id)
    return render(req, 'contracts_details.html', {'contract': contract})


def milestonesView(req, contract_id):
    contract_num = Contract.objects.get(id=contract_id).num
    try:
        contract_updates = ContractUpdate.objects.get(
            contract_id=contract_id).order_by('-event_time')
    except ContractUpdate.DoesNotExist:
        contract_updates = None
    return render(req, 'milestones.html', {'contract_num': contract_num, 'contract_updates': contract_updates})


def service_pView(req):
    return render(req, 'service_provider.html')


def notesView(req):
    return render(req, 'notes.html')


def contactsView(req):
    return render(req, 'contacts.html')
