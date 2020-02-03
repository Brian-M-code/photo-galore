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
        
    @classmethod
    def get_all_categories(cls):
        category = cls.objects.all()
        return category
    
    @classmethod
    def find(cls,categ):
        categs = cls.objects.filter(category__icontains=categ)
        return category
        
    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()
             
    def __str__(self):
        return self.category
    
class Location(models.Model):
    location_name = models.CharField(max_length = 30)
    
    def create_location(self):
        self.create()
        
    def save_location(self):
        self.save()
        
    def delete_location(self):
        self.delete()
    
     
    def __str__(self):
        return self.location
    
class Description(models.Model):
    editor = models.ForeignKey(Editor)
    image_description = models.CharField(max_length =130)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length =30)
    category = models.ForeignKey(Category) 
    editor = models.ForeignKey(Editor)
    location = models.ForeignKey(Location)
    image_description = models.ManyToManyField(Description)
    
    
    def save_image(self):
        self.save()
        
    @classmethod    
    def all_images(cls):
        images = cls.objects.all()
        return images
        
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category=search_term).all()
        return images
    
    def __str__(self):
        return self.name
    

    
    
    
