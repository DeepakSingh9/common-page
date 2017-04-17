# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from django.utils import timezone
# Create your views here.


def articles_list(request):
    posts=Post.objects.all()
    return render(request,'articles/index.html',{'posts':posts})


def User_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)


        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/articles/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print 'invalid login details :{0},{1}'.format(username,password)
            return HttpResponse("invalid login details")



    return render(request,'articles/login.html',{})


@login_required()
def User_Logout(request):
    logout(request)

    return HttpResponseRedirect('/articles/')


def AddPost(request):
    form=AddPostForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            post=form.save(commit=False)
            post.name=request.user
            post.publish=timezone.now()
            post.save()
            return redirect('articles_list')
    else:
        form=AddPostForm()
    return render(request,'articles/addpost.html',{'form':form})