from django.shortcuts import render


def indexView(req):
    return render(req, 'index.html')
