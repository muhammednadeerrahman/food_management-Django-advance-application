import datetime 
import json

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404

from main.decorators import allow_self
from main.functions import generate_form_errors
from planner.models import Student
from planner.forms import OrderForm
from planner.models import Meal, Order

@login_required(login_url = "/user/login/")
def planner (request):

    breakfast = Meal.objects.filter(food_type = "breakfast")
    lunch = Meal.objects.filter(food_type = "lunch")
    snack = Meal.objects.filter(food_type = "snack")
    dinner = Meal.objects.filter(food_type = "dinner")

    today = datetime.date.today()
    start_date =today
    next_7_days = [today + datetime.timedelta(days=i) for i in range(7)]
    
    queryset = Order.objects.filter(student__user = request.user,is_deleted=False).values_list("selected_date", flat=True,)
    # selected_date = [date.strftime('%b. %d, %Y') for date in queryset]
    selected_date = list(queryset)

    print(next_7_days)
    print(selected_date)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
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
        # data = {
        #     "selected_date" : "2023-07-03",
        #     "selected_breakfast" : "idli",
        #     "selected_lunch" : "meals",
        #     "selected_snack" : "vada",
        #     "selected_dinner" : "chicken curry",

        # }
        form = OrderForm()
           
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
def my_orders(request):
    order = Order.objects.filter(student__user = request.user,is_deleted = False )
    today = datetime.date.today()
    queryset = Order.objects.filter(student__user = request.user,is_deleted=False).values_list("selected_date", flat=True)
    # selected_date = [date.strftime('%b. %d, %Y') for date in queryset]
    list_date = list(queryset)
    required_date = [d for d in list_date if d >= today]

    print(required_date )


    context = {
        "title" : "my orders",
        "order" : order,
        "today" : today,
        "required_date" : required_date

    }
    return render(request,"planner/my_orders.html",context = context )


@login_required(login_url = "/user/login/")
@allow_self
def delete_order(request,id):
    instance = get_object_or_404(Order,id=id)
    instance.is_deleted = True
    instance.save()
    request_data = {
        "title" : "successfully deleted",
        "message" : "Order deleted successfully",
        "status" : "success",
    }
    return HttpResponse(json.dumps(request_data),content_type = "application/json")



@login_required(login_url="/user/login/")
@allow_self
def edit_order(request,id):
    instance = get_object_or_404(Order,id=id)
    breakfast = Meal.objects.filter(food_type = "breakfast")
    lunch = Meal.objects.filter(food_type = "lunch")
    snack = Meal.objects.filter(food_type = "snack")
    dinner = Meal.objects.filter(food_type = "dinner")

    today = datetime.date.today()
    start_date =today
    next_7_days = [today + datetime.timedelta(days=i) for i in range(7)]
    
    queryset = Order.objects.filter(is_deleted=False).values_list("selected_date", flat=True,)
    # selected_date = [date.strftime('%b. %d, %Y') for date in queryset]
    selected_date = list(queryset)

    print(next_7_days)
    if request.method == 'POST':
        form = OrderForm(request.POST,instance = instance)
        if form.is_valid():
            instance = form.save(commit=False)
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
            error_message = generate_form_errors(form)
            response_data = {
                "message" :str(error_message),
                "title" :"please check",
                "status" : "error",
                "stable" : "yes"

            }
            return HttpResponse(json.dumps(response_data),content_type = "application/javascript")  
        
    else:
        
        form = OrderForm(instance = instance)
        context = {
                "title" : "Make order",
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

        return render (request, "planner/edit_order.html",context = context)