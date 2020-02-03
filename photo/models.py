from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)
    
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
        
    def save_editor(self):
        self.save()
        
    def delete_editor(self):
        self.delete()  
        
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    def create_category(self):
        self.create()
        
    def save_category(self):
        self.save()
        
    def delete_category(self):
        self.delete()
     
    def __str__(self):
        return self.category_name
    
class Location(models.Model):
    location_name = models.CharField(max_length = 30)
    
    def create_location(self):
        self.create()
        
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
     
    def __str__(self):
        return self.location_name
class Description(models.Model):
    editor = models.ForeignKey(Editor)
    image_description = models.CharField(max_length =30)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images')
    image_name = models.CharField(max_length =30)
    category = models.ForeignKey(Category) 
    editor = models.ForeignKey(Editor)
    location = models.ForeignKey(Location)
    image_description = models.ManyToManyField(Description)
    
    
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image

    
    
    
