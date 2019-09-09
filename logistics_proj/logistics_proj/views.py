from django.shortcuts import render


def loginView(req):
    return render(req, 'login.html')

def resetpassView(req):
    return render(req, 'reset_password.html')