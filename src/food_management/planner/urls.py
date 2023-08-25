from django.urls import path
from planner import views

app_name = "planner"

urlpatterns = [
    path('planner/',views.planner, name = "planner"),
    path('my_orders/',views.my_orders, name = "my_orders"),
    path('sample/',views.sample, name = "sample"),
    path('delete/<int:id>/',views.delete_order, name = "delete_order"),
    path('edit/<int:id>/',views.edit_order, name = "edit_order"),

]
