from django.db import models


FOOD_TYPE = (
    ("breakfast", "Breakfast") ,
    ("lunch", "Lunch") ,
    ("snack", "Snack") ,
    ("dinner", "Dinner") ,
)
class Student(models.Model):
    name = models.CharField(max_length=100)
    profile_image = models.FileField(upload_to= "planner/profile/", blank=True,null=True)
    user = models.OneToOneField("auth.User",on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Meal(models.Model):
    food_image = models.ImageField(upload_to="breakfast/")
    dish_name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=128,choices=FOOD_TYPE)

    def __str__(self):
        return self.dish_name


class booking (models.Model):


    current_time = models.DateTimeField()
    is_draft = models.BooleanField(default=False)