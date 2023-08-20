from django import forms
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["username","password","email","first_name","last_name"]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs={"placeholder" : "enter password"}),
             "username" : forms.widgets.TextInput(attrs = {"placeholder" : "enter username"}),
             "first_name" : forms.widgets.TextInput(attrs = {"placeholder" : "enter firstname"}),
             "last_name" : forms.widgets.TextInput(attrs = {"placeholder" : "enter lastname"}),
             "email" : forms.widgets.EmailInput(attrs = {"placeholder" : "enter email"}),
        }