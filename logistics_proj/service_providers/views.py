from django.shortcuts import render

# Create your views here.


def indexView(req):
    return render(req, 'index.html')
