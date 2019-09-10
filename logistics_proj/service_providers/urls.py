from django.contrib import admin
from django.urls import path

from . import views as spViews

app_name = 'service_providers'
urlpatterns = [
    path('', spViews.contractsView, name="contracts"),
    path('contracts/<int:pk>/', spViews.contractsDetailsView, name="contracts"),
    path('n/', spViews.notesView, name="notes"),
    path('a/', spViews.contactsView, name="contacts"),
    path('b/', spViews.service_pView, name="service_p"),
]
