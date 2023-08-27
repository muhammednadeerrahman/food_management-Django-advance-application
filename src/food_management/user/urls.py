from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('login/',views.login, name = "login"),
    path('logout/',views.logout, name = "logout"),
    path('signup/',views.signup, name = "signup"),
    path('view_profile/',views.view_profile, name = "view_profile"),
    path('edit/',views.edit, name = "edit"),
    # path('student_details/',views.student_details, name = "student_details"),
]
