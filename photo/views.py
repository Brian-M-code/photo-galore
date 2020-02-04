from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Image, Category

# Create your views here.
def index(request):
    images = Image.objects.all()
    categories = Category.get_all_categories()
    return render (request, 'index.html', {"images":images, "categories":categories})
def photo_today(request):
    date = dt.date.today()
    # images = Image.get_images()
    return render(request, 'all-photo/today-photo.html', {"date": date,"image":image})

def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def search_results(request):
    
    if 'images' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_category = category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-photo/search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-photo/search.html',{"message":message})
    
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/today-photo.html", {{"image":image}})