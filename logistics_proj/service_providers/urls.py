from django.contrib import admin
from django.urls import path

from . import views as spViews

app_name = 'service_providers'
urlpatterns = [
    path('', spViews.contractsView, name="contracts"),
    path('contracts/<int:contract_id>/milestones',
         spViews.milestonesView, name="milestones"),
    path('contracts/<int:contract_id>/', spViews.contractsDetailsView,
         name="contracts_details"),
    path('sp/', spViews.service_pView, name="service_p"),
    path('sp/notes/', spViews.notesView, name="notes"),
    path('sp/contacts/', spViews.contactsView, name="contacts"),
]
