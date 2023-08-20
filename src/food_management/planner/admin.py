from django.contrib import admin
from planner.models import Student, Meal



admin.site.register(Student)

class MealAdmin(admin.ModelAdmin):
    list_display = ["dish_name","food_type",]
admin.site.register(Meal)

