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
        # Creating a new category and saving it
        self.brian= Editor(first_name = 'brian', last_name ='Mutuma', email ='mutuma@gmail.com')
        self.brian.save_editor()

        # Creating a new category and saving it
        self.new_category = Category(name = 'testing', editor = self.brian)
        self.new_category.save()

        self.new_location= Location(name = 'nairobi',editor = self.brian)
        self.new_location.save()

        self.new_image.category.location.add(self.new_category)

    def tearDown(self):
        Editor.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
        
        
class LocationTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.brian= Editor(first_name = 'brian', last_name ='Mutuma', email ='mutuma@gmail.com')
        self.brian.save_editor()

        # Creating a new tag and saving it
        self.new_location = Location(name = 'nairobi', editor = self.brian)
        self.new_location.save()

        self.new_image.category.location.add(self.new_location)

    
class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.brian= Editor(first_name = 'brian', last_name ='Mutuma', email ='mutuma@gmail.com')
        self.brian.save_editor()

        # Creating a new tag and saving it
        self.new_image = Image(id ='', category = 'art', location = 'nairobi' editor = self.brian)
        self.new_image.save()

        self.new_image.category.location.description.add(self.new_image)
        
    def test_save_method(self):
        self.new_image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(images) > 0)
        
    def test_get_images(self):
        images = Image.get_image()
        image = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
    def test_update_method(self):
        self.new_image.save_image()
        self.new_image.update_image()
        image = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
    def test_get_images_method(self):
        self.new_image.save_image()
        self.new_image.get_image()
        image = Image.objects.get(pk='')
        self.assertTrue(len(images) == 0)
        
    def test_search_image_method(self):
        self.new_image.save_image()
        self.new_image.search_image()
        image = Image.objects.filter(category='art')
        self.assertTrue(len(images) == 0
                        
    def test_filter_image_method(self):
        self.new_image.save_image()
        self.new_image.filter_image()
        image = Image.objects.filter(location='nairobi')
        self.assertTrue(len(images) == 0
                        
                    
        