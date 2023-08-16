from django.urls import path
from planner import views

app_name = "planner"

urlpatterns = [
    path('planner/',views.planner, name = "planner"),

]
