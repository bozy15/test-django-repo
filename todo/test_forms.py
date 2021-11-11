from django.test import TestCase
from .forms import ItemForm

# Test the ItemForm
class TestItemForm(TestCase):  # TestCase is a class from Django

    # Test that the ItemForm is valid
    def test_item_name_is_required(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_field_is_not_required(self):
        form = ItemForm({"name": "Test Todo Item"}) # Test Todo Item is not required
        self.assertTrue(form.is_valid()) # Test the ItemForm

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm() # Test the ItemForm
        self.assertEqual(form.Meta.fields, ["name", "complete"]) # Test the fields
