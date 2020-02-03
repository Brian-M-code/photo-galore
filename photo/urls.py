from django.conf.urls import url
from . import views

urlpatterns=[
    url('^today/$',views.photo_today,name='photoToday'),
    url(r'^search/', views.search_results, name='search_results')
]