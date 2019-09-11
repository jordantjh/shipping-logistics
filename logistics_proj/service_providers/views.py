from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
# Create your views here.


def contractsView(req):
    return render(req, 'contracts.html')


def contractsDetailsView(req, pk):
    return render(req, 'contracts_details.html')


def service_pView(req):
    return render(req, 'service_provider.html')


def notesView(req):
    notes = SPNote.objects.all()
    return render(req, 'notes.html', {'notes': notes})



def noteDetailsView(req, pk):
    note = get_object_or_404(SPNote, pk=pk)
    return render(req, 'note_details.html', {'note': note})



def contactsView(req):
    contacts = SPContact.objects
    return render(req, 'contacts.html', {'contacts': contacts})


def contactDetailsView(req, pk):
    return render(req, 'contacts_details.html')


def noteAdd(req):
    if req.method == 'POST':
        print("In post")
        if req.POST.get('content') and req.POST.get('author'):
            note = SPNote()
            print("object created")
            note.content = req.POST.get('content')
            note.author = req.POST.get('author')
            note.save()
            print("saved")


    return redirect(req, 'note_details.html')


