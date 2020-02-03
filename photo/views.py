from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def photo_today(request):
    date = dt.date.today()
    images = Image.get_images()
    return render(request, 'all-photo/today-photo.html', {"date": date,"photo":photo})

def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):
    
    if 'images' in request.GET and request.GET["image"]:
        search_term = request.GET.get("category")
        searched_category = category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photo/search.html',{"message":message})