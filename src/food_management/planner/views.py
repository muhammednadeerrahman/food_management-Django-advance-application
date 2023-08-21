import datetime 

from django.shortcuts import render

from planner.models import Meal
# from planner.forms import BookingForm

def planner (request):
    breakfast = Meal.objects.filter(food_type = "breakfast")
    lunch = Meal.objects.filter(food_type = "lunch")
    snack = Meal.objects.filter(food_type = "snack")
    dinner = Meal.objects.filter(food_type = "dinner")
    selected_date = None
    today = datetime.datetime.today()
    start_date =today
    next_7_days = [today + datetime.timedelta(days=i) for i in range(7)]
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')

        
    context ={
        "start_date" : start_date,
        "today" : today,
        "next_7_days": next_7_days,
        "breakfast" : breakfast,
        "lunch" : lunch,
        "snack" : snack,
        "dinner" : dinner,

        }

    return render (request, "planner/planner.html", context = context)


# def profile_form_view(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Handle successful form submission
#     else:
#         form = BookingForm()
#         context ={
#             'form': form

#         }
#     return render(request, 'profiles/profile_form.html',context = context)