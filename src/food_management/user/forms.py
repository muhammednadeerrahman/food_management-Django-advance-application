from django import forms
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["username","password",]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs={"placeholder" : "enter password"}),
             "username" : forms.widgets.TextInput(attrs = {"placeholder" : "enter username"}),
             "firstname" : forms.widgets.TextInput(attrs = {"placeholder" : "enter firstname"}),
             "lastname" : forms.widgets.TextInput(attrs = {"placeholder" : "enter lastname"}),
             "email" : forms.widgets.EmailInput(attrs = {"placeholder" : "enter email"}),
             "mob_number" : forms.widgets.NumberInput(attrs = {"placeholder" : "enter mob_number"}),
        }