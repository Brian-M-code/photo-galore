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
        category = cls.objects.filter(category__icontains=categ)
        return category
        
    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()
             
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
    image_description = models.CharField(max_length =130)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    headimage = ImageWithThumbsField(upload_to='images/', blank=True, sizes=((200,200),(400,400)))
    image_name = models.CharField(max_length =30)
    category = models.ForeignKey(Category) 
    editor = models.ForeignKey(Editor)
    location = models.ForeignKey(Location)
    image_description = models.ManyToManyField(Description)
    
    def __str__(self):
        return str(self.image)
    
    
    def save_image(self):
        self.save()
        
    def get_image(self):
        self.get_image()
        
    def update_image(self):
        self.update_image()
        
    def search_image(self):
        self.search_image()
        
    def filter_image(self):
        self.filter_image()
        
    def delete_image(self):
        self.delete_image()
           
    @classmethod    
    def all_images(cls):
        images = cls.objects.all()
        return images
    
        
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category=search_term).all()
        return str(image)
    
    def __str__(self):
        return str(self.image)
    

    
    
    
