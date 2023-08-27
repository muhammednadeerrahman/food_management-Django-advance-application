from django import forms
from django.contrib.auth.models import User
from planner.models import Student


class StudentForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["username","password","email","first_name","last_name",]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs={"placeholder" : "enter password"}),
             "username" : forms.widgets.TextInput(attrs = {"placeholder" : "enter username"}),
             "first_name" : forms.widgets.TextInput(attrs = {"placeholder" : "enter firstname","required" : "required"}),
             "last_name" : forms.widgets.TextInput(attrs = {"placeholder" : "enter lastname","required" : "required"}),
             "email" : forms.widgets.EmailInput(attrs = {"placeholder" : "enter email","required" : "required"}),
        }
        error_messages= {

            'first_name' : {
                "required" : "enter first name"
                },
            'last_name' : {
                    "required" : "enter last name"
                    },
            'email' : {
                    "required" : "select a email"
                    },
        }
        


class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["profile_image","student_id","mob_number",]
        
       