from django.shortcuts import render,reverse
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout
from django.contrib.auth.models import User

from planner.models import Student
from main.functions import generate_form_errors
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
   else:
            context = {
                "title" : "sign in | Meal Planner "

            }
            return render (request, "users/login.html",context = context)
   

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("user:login"))


def signup(request):
   if request.method == "POST" :
        form = StudentForm(request.POST)
        if form.is_valid():
           instance = form.save(commit=False)
           user = User.objects.create_user(
              username = instance.username,
              password = instance.password,
              first_name = instance.first_name,
              last_name = instance.last_name,
              email = instance.email,
           )
           student = Student.objects.create(name = instance.First_name,user=user)
           user = authenticate(request,username=instance.username, password=instance.password)
           auth_login(request, user)
           return HttpResponseRedirect(reverse("user:login"))
        else:
           message = generate_form_errors(form)
           context = {
                "title" : "student signup",
                "error" : True,
                "message" : message,
                "form" : form
            }
           return render(request, "users/signup.html",context = context)
   else:
      
    form = StudentForm()
    context = {
        "title" : "student Signup",
        "form" : form,
    }
    return render (request,"users/signup.html", context = context) 
