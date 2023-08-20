from django.shortcuts import render
from planner.models import Meal


def index(request) :
    meal = Meal.objects.filter(food_type="breakfast")
    lunch = Meal.objects.filter(food_type="lunch")
    snack = Meal.objects.filter(food_type="snack")
    dinner = Meal.objects.filter(food_type="dinner")
    context = {
        "title" : "meal planner",
        "meal" : meal,
        "dinner" : dinner,
        "snack" : snack,
        "lunch" : lunch,
    }
    return render (request, "web/index.html" , context = context)
