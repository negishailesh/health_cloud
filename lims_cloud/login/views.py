# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth import  authenticate , login

class LoginView(View):
    """
    """
    http_method_names = [ 'get' , 'post']
    context = {}
    def post(self, request):
	print "INSIDE POST"
        username = str(request.POST['username'])
        password = str(request.POST['password'])
	user = authenticate(username = username, password = password)
	if user is not None:
	    print "INSIDE AUTHENTICATE"
	    if user.is_active:
		print "INSIDE ACTIVATION"
		login(request, user)
		return HttpResponseRedirect('/rango/')
	    else:
		print "INSIDE USER DISABLE"
		context = {"error" : "Your Rango account is disabled."}
		return render(request, 'login/login.html', context)
	else:
	    print "INSIDE INVALID"
	    context = {"error" : "Invalid login details supplied."}
	    return render(request, 'login/login.html', context)

    def get(self , request):
	print "INSIDE GET"
	context = {}
        return render(request, 'login/login.html', context)






