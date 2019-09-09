from django.contrib import admin
from django.urls import path

from . import views as spViews

app_name = 'service_providers'
urlpatterns = [
    path('a/', spViews.contractsView, name="contracts"),
    path('b/', spViews.service_pView, name="service_p"),

]
