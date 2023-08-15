from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login

def login(request):
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")      

      if username and password :
         user = authenticate(request, username = username, password = password )
         if user is not None :
            auth_login(request, user)
            return(HttpResponseRedirect("/"))

   
   context = {
      "title" : "student Login",
      "error" : True,
      "message" : "Invalid Credentials"
      
   }
   return  render(request, "users/login.html", context = context)


def signup(request):
   context = {
      "title" : "student Signup",
      
      
   }
   return render (request,"users/signup.html", context = context) 
