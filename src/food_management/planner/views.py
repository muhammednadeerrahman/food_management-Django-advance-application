from django.shortcuts import render

def planner (request):
    context = {
        "title" : "plan your meal"
    }
    return render (request, "planner/planner.html", context = context)