from django.contrib import admin
from .models import Editor, Category, Location, Image

# Register your models here.
admin.site.register(Editor)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)
