import json

from django.shortcuts import render,reverse
from django.http.response import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login , logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from planner.models import Student, Order
from main.functions import generate_form_errors
from user.forms import StudentForm,UserForm

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
           Student.objects.create(name = instance.first_name +" "+instance.last_name, user=user)
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


@login_required(login_url="/user/login/")
def view_profile(request) :
    user = request.user
    student = user.student

    if request.method == "POST":
        mob_number = request.POST.get('mob_number')
        student_id = request.POST.get('student_id')

        if mob_number:
            student.mob_number = mob_number
        if student_id:
            student.student_id = student_id

        if request.FILES.get('profile_image'):
            student.profile_image = request.FILES['profile_image']
        student.save()
        response_data = {
                "message" :"sucessfully profile_updated",
                "title" :"profile updated",
                "status" : "success",
                "redirect_url" : "/",
                "redirect" : "yes"
            }
        return HttpResponse(json.dumps(response_data),content_type = "application/javascript")  
    context = {
            "title": "My Profile",
            "student": student,
    }
    return render(request, "users/view_profile.html", context=context)


def edit(request):
    user = request.user
    student = user.student 

    if request.method == "POST":
        userform = UserForm(request.POST,request.FILES, instance=student)
        if userform.is_valid():
            instance = userform.save(commit=False)
            instance.save()
            response_data = {
                "message" :"sucessfully submitted",
                "title" :"sucessfully submitted",
                "status" : "success",
                "redirect_url" : "/",
                "redirect" : "yes"
            }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
        else:
            response_data = {
                "message" : "something error",
                "title" :"please check",
                "status" : "error",
                "stable" : "yes"

            }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
    else:
        userform = UserForm(instance=student)

    context = {
        "title": "Edit Profile",
        "userform": userform,
    }
    return render (request, "users/edit.html",context=context)