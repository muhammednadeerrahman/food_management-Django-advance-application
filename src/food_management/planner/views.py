import datetime 
import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from main.functions import generate_form_errors
from planner.models import Student
from planner.forms import OrderForm
from planner.models import Meal, Order


def planner (request):

    breakfast = Meal.objects.filter(food_type = "breakfast")
    lunch = Meal.objects.filter(food_type = "lunch")
    snack = Meal.objects.filter(food_type = "snack")
    dinner = Meal.objects.filter(food_type = "dinner")

    today = datetime.date.today()
    start_date =today
    next_7_days = [today + datetime.timedelta(days=i) for i in range(7)]

    queryset = Order.objects.values_list("selected_date", flat=True)
    # selected_date = [date.strftime('%b. %d, %Y') for date in queryset]
    selected_date = list(queryset)

    print(next_7_days)
    print(selected_date)


    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            if not Student.objects.filter(user=request.user).exists():
                student = Student.objects.create(user = request.user,name = request.user.last_name)
            else:
                student = request.user.student

            instances = form.save(commit=False) 
            instances.student = student
            instances.save()

            response_data = {
                "message" :"sucessfully submitted",
                "title" :"sucessfully submitted",
                "status" : "success",
                "redirect_url" : "/",
                "redirect" : "yes"
            }

            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
        else:
            error_message = generate_form_errors(form)

            response_data = {
                    "message" :str(error_message),
                    "title" :"please check something error occured",
                    "status" : "error",
                    "redirect_url" : "/",
                    "redirect" : "yes"
                }

            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
    
    else: 
        data = {
            "selected_date" : "2023-07-03",
            "selected_breakfast" : "idli",
            "selected_lunch" : "meals",
            "selected_snack" : "vada",
            "selected_dinner" : "chicken curry",

        }
        form = OrderForm(initial=data)
           
    context ={
        "form" : form,
        "start_date" : start_date,
        "today" : today,
        "next_7_days": next_7_days,
        "breakfast" : breakfast,
        "lunch" : lunch,
        "snack" : snack,
        "dinner" : dinner,
        "selected_date" : selected_date

        }

    return render (request, "planner/planner.html", context = context)

@login_required(login_url = "/user/login/")
def sample(request) :
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            if not Student.objects.filter(user=request.user).exists():
                student = Student.objects.create(user = request.user,name = request.user.last_name)
            else:
                student = request.user.student

            instance = form.save(commit=False)
            instance.student = student
            instance.save()

            response_data = {
                "message" :"sucessfully submitted",
                "title" :"sucessfully submitted",
                "status" : "success",
                "redirect_url" : "/",
                "redirect" : "yes"
            }

            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")
        else :

            error_message = generate_form_errors(form)

            response_data = {
                    "message" :str(error_message),
                    "title" :"please check something error occured",
                    "status" : "error",
                    "redirect_url" : "/",
                    "redirect" : "yes"
                }

            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")

    else:
        form = OrderForm()

        context ={
            "title" : "sample",
            "form" : form
        }
    return render (request, "planner/sample.html",context = context)