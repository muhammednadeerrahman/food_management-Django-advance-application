from django.shortcuts import render


def index(request) :
    context = {
        "title" : "meal planner"
    }
    return render (request, "web/index.html" , context = context)
