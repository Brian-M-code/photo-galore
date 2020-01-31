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

class Image(models.Model):
    image = models.ImageField(upload_to = 'images')
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    image_category = models.ForeignKey(Category) 
    editor = models.ForeignKey(Editor)
# class Category(models.Model):
#     category_name = models.