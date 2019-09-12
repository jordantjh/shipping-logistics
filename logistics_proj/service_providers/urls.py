from django.contrib import admin
from django.urls import path

from django.contrib.auth.decorators import login_required

from . import views as spViews

app_name = 'service_providers'
urlpatterns = [
    path('', login_required(spViews.contractsView), name="contracts"),
    path('contracts/<int:contract_id>/milestones',
         login_required(spViews.milestonesView), name="milestones"),
    path('contracts/<int:contract_id>/',
         login_required(spViews.contractsDetailsView), name="contracts_details"),
    path('sp/', login_required(spViews.service_pView), name="service_p"),
    path('sp/notes/<int:note_id>/',
         login_required(spViews.noteDetailsView), name="note_details"),
    path('sp/notes/', login_required(spViews.notesView), name="notes_list"),
    path('sp/contacts/', login_required(spViews.contactsView), name="contacts_list"),
    path('sp/contacts/<int:contact_id>/',
         login_required(spViews.contactDetailsView), name="contact_details"),
    path('sp/notes/new/', login_required(spViews.noteAdd), name="note_new"),
    path('sp/contacts/new/', login_required(spViews.contactAdd), name="contacts_new"),
    path('passwordchanged', login_required(
        spViews.passwordchangedView), name="passwordchanged"),

]
