from django.shortcuts import render

# Create your views here.


def contractsView(req):
    return render(req, 'contracts.html')
