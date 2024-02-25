from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User

from django.views import View


def about(request):
    return render(request, "about.html")


def home(request):
    user_data = User.objects.all()
    data_send = request.session.pop('data_send', False)
    success = {"context":user_data,'data_send':data_send}
    return render(request, 'home.html',success)

class UserPro(View):
    def get(self, request, id):
        user_data = User.objects.get(id = id)
        return render(request, 'user_pro.html',{"context":user_data})
    
class Code(View):
    def get(self, request, id):
        code_objs = User.objects.get(id = id).user_code.all()
        print(code_objs,"----------------code_objs>>>>>>>>>")
        return render(request, 'user_code.html',{"context":code_objs})


def vali(request):
    if request.method == 'POST':
        name = request.POST.get('name')
    user = {'name':name}
    return render(request,'vali.html',user)



def register(request):
    data_send = False
    
    
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone_no = request.POST.get('phone')
        data_send = True
        new_user = User(First=fname, last=lname, email=email, phone_no=phone_no)
        new_user.save()
        request.session['data_send'] = data_send
        return redirect('/dsa/')
    else:
        print("no data received")
    users= User.objects.all()
    users_data = {"context":users,'data_send':data_send}
    return render(request,"home.html",users_data)
    