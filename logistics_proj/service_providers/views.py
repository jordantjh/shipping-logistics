from django.shortcuts import render

# Create your views here.


def contractsView(req):
    return render(req, 'contracts.html')
def service_pView(req):
    return render(req, 'service_provider.html')

def contactsView(req):
    return render(req, 'contacts.html')