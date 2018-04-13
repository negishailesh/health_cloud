# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class LoginView(View):
    """
    """
    http_method_names = ['post', 'get']
    def post(self, request):
        pass
    def get(self , request):
	context = {}
        return render(request, 'login/login.html', context)
