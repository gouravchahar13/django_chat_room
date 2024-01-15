"""
URL configuration for chatting_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #home
    path('',home,name='home'),
    path('signup/',Signup_view,name='signup'),
    path('login/',login_page,name='login_pg'),
    
    #user
    path('profile/<str:username>',user_profile,name='profile'),
    path('logout/<str:username>',log_out),
    path('settings/<str:username>',settings_user,name='settings'),
    path('delete/<str:username>',delete_user),
    path('mail/<str:username>',recov_mail),
    
    
    #chatroom
    path('chatroom/',chat_room,name='chatroom'),
    path('deletepost/<int:id>',deletepost),
    
]
urlpatterns += [
    path('captcha/', include('captcha.urls')),
]
