from django.test import TestCase
from .models import Item

# Create your tests here.

# Test the models
class TestModels(TestCase):# TestCase is a class that comes with Django

    def test_done_defaults_to_false(self): # Test that the done defaults to false
        item = Item.objects.create(name="Test Todo Item") # Create an item
        self.assertFalse(item.complete) # Test when item is completed is set to false

    def test_item_string_method_returns_name(self): # Test the string method
        item = Item.objects.create(name="Test Todo Item") # Create an item
        self.assertEqual(str(item), "Test Todo Item") # Test the item created is returned as a string
