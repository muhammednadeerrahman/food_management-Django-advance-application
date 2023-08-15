from django import forms
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
    class Meta :
        model = User
        fields = ["username","password",]
        widgets = {
            "password" : forms.widgets.PasswordInput(attrs={"placeholder" : "enter password"}),
             "username" : forms.widgets.TextInput(attrs = {
                "placeholder" : "enter username"
            }),
        }