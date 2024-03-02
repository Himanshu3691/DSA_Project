from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User,UserCode

from django.views import View

name = 'test'
email = 'test@gmail.com'
def about(request):
    return render(request, "about.html")

def login_status(name = 'test', email = 'test@gmail.com'):
    return name, email
def login_data():
    name, email = login_status()
    print(name,email,"-----------------")


def home(request):
    user_data = User.objects.all()
    data_send = request.session.pop('data_send', False)
    success = {"context":user_data,'data_send':data_send}
    return render(request, 'home.html',success)

class UserPro(View):
    def get(self, request, id):
        global name,email
        login = False
        user_data = User.objects.get(id = id)
        user_mail = User.objects.get(id = id).email
        name,email = name.lower(),email.lower(  )
        # print(name,email,user_data,user_mail,"-----------------")
        if name == user_data.First and email == user_mail:
            login = True
            name = 'test'
            email = 'test@gmail.com'
        data = {"context":user_data,'login':login}
       
        # print(name,email,"-----------------global wali ahi is baaar")
        return render(request, 'user_pro.html',data)
class Code(View):
    def get(self, request, id):
        code_objs = User.objects.get(id = id).user_code.all()
        user_name = User.objects.get(id = id).First
        return render(request, 'user_code.html',{"context":code_objs,'user_name':user_name})


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
        # sti = 'this is as fgsad'
        fname = fname.lower()
        lname = lname.lower()
        email  = email.lower()
        phone_no =  phone_no.lower()
        new_user = User(First=fname, last=lname, email=email, phone_no=phone_no)
        new_user.save()
        request.session['data_send'] = data_send
        return redirect('/dsa/')
    else:
        print("no data received")
    users= User.objects.all()
    users_data = {"context":users,'data_send':data_send}
    return render(request,"home.html",users_data)
    
def coderegister(request,id):
    if request.method == 'POST':
        day = request.POST.get('day')
        code = request.POST.get('code')
        id = id
        # print(id)
        # print(day,code)
        user_data = User.objects.get(id = id)
        # print(user_data)
        new_code = UserCode(user_code = user_data, day = day , code = code)
        new_code.save()
        return redirect('/dsa/')
    return render(request,'user_pro.html')
    
    
def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        search = search.lower()
        user_data = User.objects.filter(First = search)
        print(user_data,"-----------------user_data")
        return render(request, 'home.html',{"context":user_data})
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        global name,email
        first = request.POST.get('first')
        email = request.POST.get('email')
        # print(email,first)
        name = first # do not use these global variables
        email = email # do not use these global variables
        # print(email,name,"-----------------")
        user_data = User.objects.filter(First = first.lower(),email = email)
        # print(user_data,"-----------------user_data")
    
        if user_data:
            return redirect('/dsa/')
        else:
            return HttpResponse("Invalid user")
    return redirect('/dsa/')