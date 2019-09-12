from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.urls import reverse

def loginView(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username ,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('sp:contracts'))
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def logoffView(request):
    logout(request)
    return redirect('login')
