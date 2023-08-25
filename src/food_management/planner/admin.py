from django.contrib import admin
from planner.models import Student, Meal, Order


admin.site.register(Student)

class MealAdmin(admin.ModelAdmin):
    list_display = ["dish_name","food_type",]
admin.site.register(Meal, MealAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ["selected_date","selected_breakfast","selected_lunch","selected_snack","selected_dinner"]

admin.site.register(Order,OrderAdmin )



