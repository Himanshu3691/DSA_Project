from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("this is the main page")
    return render(request,'index.html')