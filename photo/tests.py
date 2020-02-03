from django.test import TestCase
from .models import Editor, Category, Location, Image

# Create your tests here.
class EditorTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.brian= Editor(first_name = 'Brian', last_name ='Mutuma', email ='mutuma@gmail.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.brian,Editor))
        
    # Testing Save Method
    def test_save_method(self):
        self.brian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
     # Testing Delete Method
    def test_delete_method(self):
        self.brian.save_editor()
        self.brian.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.category.create
    
class LocationTestClass(TestCase):
    
class ImageTestClass(TestCase):
        