from django.shortcuts import render
from django.http.response import HttpResponse


def login(request):
   context = {
      
   }
   return  render(request, "users/login.html", context = context)
