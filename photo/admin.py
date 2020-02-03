from django.contrib import admin
from .models import Editor, Category, Location, Image, Description

# Register your models here.

class ImageAdmin(admin.ModelAdmin):

    filter_horizontal =('image_description',)
admin.site.register(Editor)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Description)
