from django.shortcuts import render


def loginView(req):
    return render(req, 'login.html')
