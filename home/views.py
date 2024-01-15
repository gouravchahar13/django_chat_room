from django.shortcuts import render,redirect
from .forms import Signup_Form,Login_form
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import chatroom
from .mail import *

# Create your views here.


def home(request):
    context={'title':"Chatting_app"}
    return render(request,'index.html',context)

# chatroom shit


@login_required(login_url='/login/')
def chat_room(request):
    if request.method=='POST':
        content=request.POST.get('post')
        username=request.POST.get('username')
        image=request.FILES['image']
        chatroom.objects.create(
            content=content,
            username =username,
            image=image,
        )
        return redirect('chatroom')
    queryset = chatroom.objects.all()
    context={'chat':queryset,'title':'chatroom'}
    return render(request,'chatroom.html',context)

def deletepost(request,id):
    deleteobj=chatroom.objects.filter(id=id)
    deleteobj[0].delete()
    return redirect('/chatroom/')


#chatroom shit ends

#signup

def Signup_view(request):
    if request.method=='POST':
        form=Signup_Form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                messages.info(request,'Invalid username')
                return redirect('signup')
            form.save()
            reg_mail()
            messages.info(request,'account created successfully')
            return redirect('signup')
        else:
            messages.info(request,'please fill the captcha correctly')
            return redirect('signup')
    context={'title':'Signup','form':Signup_Form()}
    return render(request,'register_login/signup.html',context)
    
#login
def login_page(request):
    if request.method=='POST':
        form=Login_form(request.POST)
        if form.is_valid():
            data=request.POST
            username=data.get('username')
            password=data.get('password')
            if not User.objects.filter(username=username).exists():
                messages.info(request,'Invalid username')
                return redirect('login_pg')
            user=authenticate(username=username,password=password)  
            if user is None:
                messages.info(request,'Invalid username/Password')    
                return redirect('login_pg')      
            login(request,user)
            messages.info(request,'You have successfully logged into the site')            
            return redirect('home')
        else:
            messages.info(request,'please fill the captcha correctly')
            return redirect('/login/')
    context={'title':'Login','form':Login_form()}
    return render(request,'register_login/login.html',context)

#users
@login_required(login_url='/login/')
def user_profile(request,username):
    user=User.objects.get(username=username)
    if request.method=='POST':
        data=request.POST
        username=data.get('username')
        password=data.get('password')
        user.set_password(password)
        user.username=username
        user.save()
        messages.info(request,'profile updated successfully')
        return render('profile')
    user=User.objects.filter(username=username)
    context={'title':'Profile','user':user}
    return render(request,'user/profile.html',context)

@login_required(login_url='/login/')
def log_out(request,username):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('home')

@login_required(login_url='/login/')
def settings_user(request,username):
    user=User.objects.get(username=username)
    context={'title':'Profile','user':user}
    return render(request,'user/settings.html',context)

@login_required(login_url='/login/')
def delete_user(request,username):
    u = User.objects.get(username = username)
    u.delete()
    delete_mail()
    messages.info(request, "Acoount deleted successfully")
    return redirect('home')

@login_required(login_url='/login/')
def recov_mail(request,username):
    u = User.objects.get(username = username)
    email=u.email
    mail=EmailMessage(
        subject='Recov mail',
        body='message',
        from_email=settings.EMAIL_HOST_USER,
        to=['gouravchahar1111@gmail.com'],
    )
    file=f"{settings.BASE_DIR}/abc.xlsx"
    mail.attach_file(file)
    mail.send()
    messages.info(request, "mail sent successfully")
    return redirect('home')