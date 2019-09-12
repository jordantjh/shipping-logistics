from django.contrib import admin
from django.urls import path

from . import views as spViews

app_name = 'service_providers'
urlpatterns = [
    path('', spViews.contractsView, name="contracts"),
    path('contracts/<int:contract_id>/milestones',spViews.milestonesView, name="milestones"),
    path('contracts/<int:contract_id>/', spViews.contractsDetailsView,name="contracts_details"),
    path('sp/', spViews.service_pView, name="service_p"),
    path('sp/notes/<int:note_id>/', spViews.noteDetailsView, name="note_details"),
    path('sp/notes/', spViews.notesView, name="notes_list"),
    path('sp/contacts/', spViews.contactsView, name="contacts_list"),
    path('sp/contacts/<int:contact_id>/', spViews.contactDetailsView, name="contact_details"),
    path('sp/notes/new/', spViews.noteAdd, name="note_new"),
    path('sp/contacts/new/', spViews.contactAdd, name="contacts_new"),
]
