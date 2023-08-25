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
    mob_number = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    student_id = models.CharField(max_length=15,null=True,blank=True)
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
    

class Order (models.Model):
    selected_date = models.DateField(unique=True)
    selected_breakfast = models.CharField(max_length=200)
    selected_lunch = models.CharField(max_length=200)
    selected_snack = models.CharField(max_length=200)
    selected_dinner = models.CharField(max_length=200)

    
    student = models.ForeignKey("planner.Student", on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.selected_breakfast 


