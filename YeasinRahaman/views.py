import urllib.request
import json
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from YeasinRahaman.forms import *
from django.contrib.auth.decorators import login_required


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        login(request, user)
        return redirect('home')
    else:
        context = {"form":form}
        return render(request, 'registration/register_form.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error_message': 'Username or Password Invalid login'})
    return render(request, 'registration/login.html')
@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    geourl = "https://randomuser.me/api/"
    response = urllib.request.urlopen(geourl)
    content = response.read()
    data = json.loads(content.decode("utf8"))
    return render(request, "registration/profile.html", {"data": data})
