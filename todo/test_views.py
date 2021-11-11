from django.test import TestCase
from .models import Item

# Create your tests here.

# Test the views
class TestViews(TestCase): # TestCase is a class from Django
    def test_get_todo_list(self): # test todo list
        response = self.client.get("/") # get todo list
        self.assertEqual(response.status_code, 200) # check status code is 200
        self.assertTemplateUsed(response, "todo/todo_list.html") # Test the model

    def test_get_add_item_page(self): # test add item page
        response = self.client.get("/add") # add item
        self.assertEqual(response.status_code, 200) # check status code is 200
        self.assertTemplateUsed(response, "todo/add_item.html") # test the model

    def test_get_edit_item_page(self): # test edit item page
        item = Item.objects.create(name="Test Todo Item") # create item
        response = self.client.get(f"/edit/{item.id}") # edit item
        self.assertEqual(response.status_code, 200) # check status code is 200
        self.assertTemplateUsed(response, "todo/edit_item.html") # test the model

    def test_can_add_item(self): # test add item
        response = self.client.post("/add", {"name": "Test Added Item"}) # add item
        self.assertRedirects(response, "/") # redirect to home page

    def test_can_delete_item(self): # test delete item
        item = Item.objects.create(name="Test Todo Item") # create item
        response = self.client.get(f"/delete/{item.id}") # delete item
        self.assertRedirects(response, "/") # redirect to todo list
        existing_item = Item.objects.filter(id=item.id) # get updated item
        self.assertEqual(len(existing_item), 0) # double check item is deleted

    def test_can_toggle_item(self): # test toggle item
        item = Item.objects.create(name="Test Todo Item", complete=True) # create item
        response = self.client.get(f"/toggle/{item.id}") # toggle item
        self.assertRedirects(response, "/") # redirect to todo list
        updated_item = Item.objects.get(id=item.id) # get updated item
        self.assertFalse(updated_item.complete) # check if item is not complete

    def test_can_edit_item(self): # test edit item
        item = Item.objects.create(name="Test Todo Item") # create item
        response = self.client.post(f"/edit/{item.id}", {"name": "Updated Name"}) # edit item
        self.assertRedirects(response, "/") # redirect to todo list
        updated_item = Item.objects.get(id=item.id) # get updated item
        self.assertEqual(updated_item.name, "Updated Name") # check if name was updated