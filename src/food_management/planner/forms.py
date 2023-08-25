from django import forms
from django.forms import ModelForm
from planner.models import Order

class OrderForm(ModelForm):

    class Meta : 
        model = Order
        exclude = ["student","is_draft","is_deleted",]
        widgets = {

            "selected_breakfast" : forms.TextInput(attrs ={
                "readonly":"readonly",
                "id":"selected_input_breakfast"
                }),
             "selected_lunch" : forms.TextInput(attrs ={
                "readonly":"readonly",
                "id":"selected_input_lunch"
                }),
             "selected_snack" : forms.TextInput(attrs ={
                "readonly":"readonly",
                "id":"selected_input_snack"
                }),
             "selected_dinner" : forms.TextInput(attrs ={
                "readonly":"readonly",
                "id":"selected_input_dinner"
                }),
        }
        error_messages= {
            'selected_date' : {
                "required" : "select a date"
                },

            'selected_breakfast' : {
                "required" : "select a breakfast"
                },
            'selected_lunch' : {
                    "required" : "select a lunch"
                    },
            'selected_snack' : {
                    "required" : "select a snack"
                    },
            'selected_dinner' : {
                    "required" : "select a dinner"
                    },
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['selected_date'].widget = forms.DateInput(attrs={ 
            "id":"selected_input_date",
            "readonly":"readonly",
        })


