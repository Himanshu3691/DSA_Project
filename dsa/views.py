from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User,UserCode,Variable
# from django

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
        
        user_data = User.objects.filter(id = id).first()        
        var_obj = Variable.objects.filter(user_var = user_data , login= True).first()
        if var_obj:
            data = {"context":user_data,'login':True}
        else:
            data = {"context":user_data,'login':False}
    
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
        # print(user_data,"-----------------user_data")
        return render(request, 'home.html',{"context":user_data})
    return render(request, 'home.html')
 
def login(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        email = request.POST.get('email')
        user_data = User.objects.filter(First = first.lower(),email = email).first()
        if not user_data:
            return HttpResponse("Invalid user")
        v_object = Variable.objects.filter(user_var = user_data).first()
        
        if not v_object:
            var_obj = Variable.objects.create(user_var=user_data,variable_type = 'login',variable1 = first,variable2 = email,login = True)
            return redirect('/dsa/')
    
        if v_object:
            v_object.login = True
            v_object.save()
            return redirect(f'/dsa/user_pro/{user_data.id}')
        else:
            return HttpResponse("Invalid user")
    return redirect('/dsa/')


class UserLogout(View):
    def get(self, request, id):
        
        user_data = User.objects.filter(id = id).first()        
        var_obj = Variable.objects.filter(user_var = user_data).first()
        var_obj.login = False
        var_obj.save()
      
    
        return redirect('/dsa/')
        