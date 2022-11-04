from .base import FunctionalTest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):
    """Valid items"""
    def test_cannot_add_empty_list_items(self):
        """Can`t create empty list`s"""
        """Edith opens the homepage and accidentally tries to send empty list element. 
        She presses Enter on an empty input field.
        The home page refreshes and an error message appears that says the list items must not be empty. 
        She tries again, now with some text for the item, and now it works. Oddly enough, 
        Edith decides to submit a second one. 
        empty list item She gets a similar warning on the list page 
        AND she can fix it by filling in the field with some text"""
        self.fail('Write on ME!')
