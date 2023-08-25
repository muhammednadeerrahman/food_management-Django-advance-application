from django.urls import path
from planner import views

app_name = "planner"

urlpatterns = [
    path('planner/',views.planner, name = "planner"),
    path('sample/',views.sample, name = "sample"),
    # path('profile_form_view/',views.profile_form_view, name = "profile_form_view"),

]
