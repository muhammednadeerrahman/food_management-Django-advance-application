from django.shortcuts import render
import datetime 
# from planner.forms import BookingForm

def planner (request):
    selected_date = None
    today = datetime.datetime.today()
    start_date =today
    next_7_days = [today + datetime.timedelta(days=i) for i in range(7)]
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')

        
    context ={
        "start_date" : start_date,
        "today" : today,
        "next_7_days": next_7_days,
            


        }

    return render (request, "planner/planner.html", context = context)


# def profile_form_view(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Handle successful form submission
#     else:
#         form = BookingForm()
#         context ={
#             'form': form

#         }
#     return render(request, 'profiles/profile_form.html',context = context)