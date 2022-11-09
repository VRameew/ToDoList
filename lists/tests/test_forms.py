from django.test import TestCase
from lists.forms import ItemForm


class ItemFormTest(TestCase):
    """Test fjrms and lists validation"""
    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())
