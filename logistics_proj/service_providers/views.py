from django.shortcuts import render

from .models import Contract, ContractUpdate

# Create your views here.


def contractsView(req):
    contracts = Contract.objects.all()
    return render(req, 'contracts.html', {'contracts': contracts})


def contractsDetailsView(req, contract_id):
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
