from django.http import HttpResponse
from django.shortcuts import render, redirect



def index(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, 'home.html')


def vali(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    user = {'name':name}
    return render(request,'vali.html',user)