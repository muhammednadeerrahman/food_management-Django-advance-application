from django.db import models


FOOD_TYPE = (
    ("breakfast", "Breakfast") ,
    ("lunch", "Lunch") ,
    ("snack", "Snack") ,
    ("dinner", "Dinner") ,
)
# BREAKFAST = (
#     ("idli", "Idli") ,
#     ("puttu", "Puttu") ,
#     ("dosa", "dosa") ,
#     ("appam", "Appam") ,
# )

# LUNCH = (
#     ("chicken biriyani", "Chicken Biriyani") ,
#     ("meals", "Meals") ,
#     ("fried rice", "Fried Rice") ,
#     ("ghee rice and curry", "Ghee Rice and Curry") ,
# )

# SNACK = (
#     ("vada", "Vada") ,
#     ("egg puff", "Egg puff") ,
#     ("Samosa", "samosa") ,
#     ("payampori", "payampori") ,
# )

# DINNER = (
#     ("porota/chappathi with Egg Curry", "porota/chappathi with Egg Curry") ,
#     ("meals", "Meals") ,
#     ("fried rice", "Fried Rice") ,
#     ("ghee rice and curry", "Ghee Rice and Curry") ,
# )

class Student(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.FileField(upload_to= "planner/profile/", blank=True,null=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Meal(models.Model):
    food_image = models.ImageField(upload_to="breakfast/", null=True,blank=True)
    dish_name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=128,choices=FOOD_TYPE)

    meal_date = models.DateField()
    is_draft = models.BooleanField(default=False)


    def __str__(self):
        return self.dish_name


