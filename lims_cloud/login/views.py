# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import  authenticate , login
from django.contrib.auth.decorators import login_required



class LoginView(View):
    """
    user login
    """
    http_method_names = [ 'get' , 'post']
    context = {}
    def post(self, request):
        username = str(request.POST['username'])
        password = str(request.POST['password'])
	user = authenticate(username = username, password = password)
	if user is not None:
	    if user.is_active:
		login(request, user)
		#return HttpResponseRedirect('/rango/')
		return HttpResponse('You Have logged in successfully')
	    else:
		context = {"error" : "Your Rango account is disabled."}
		return render(request, 'login/login.html', context)
	else:
	    context = {"error" : "Invalid login details supplied."}
	    return render(request, 'login/login.html', context)

    def get(self , request):
	context = {}
        return render(request, 'login/login.html', context)





class CreateUser(View):
    """
    this page will only be visible to super user
    """
    http_method_names = ['get' , 'post']
    def get(self , request):
        context = {}
        return render(request, 'login/add_user.html', context)

    def post(self , request):
        pass   
