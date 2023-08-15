from django.shortcuts import render, reverse
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout
from user.forms import StudentForm

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

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("user:login"))


def signup(request):
   form = StudentForm()
   context = {
      "form" : form,
      "title" : "student Signup",
      
      
   }
   return render (request,"users/signup.html", context = context) 
