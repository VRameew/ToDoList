from .base import FunctionalTest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from unittest import skip


class ItemValidationTest(FunctionalTest):
    """Valid items"""

    def test_cannot_add_empty_list_items(self):
        """Can`t create empty list`s"""
        """Edith opens the homepage and accidentally tries to send empty list element. 
        She presses Enter on an empty input field."""
        self.browser.get(self.live_server_url)
        self.browser.find_element(by=By.ID, value='id_new_item').send_keys(Keys.ENTER)
        """The home page refreshes and an error message appears that says the list items must not be empty."""
        self.wait_for(lambda: (self.assertEqual(self.browser.find_element(by=By.CSS_SELECTOR, value='.has-error'),
                                                "You can't have an empty list item")))
        """She tries again, now with some text for the item, and now it works."""
        self.browser.find_element(by=By.ID, value='id_new_item').send_keys('Buy Milk')
        self.browser.find_element(by=By.ID, value='id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        """Oddly enough, Edith decides to submit a second one."""
        self.browser.find_element(by=By.ID, value='id_new_item').send_keys(Keys.ENTER)
        self.wait_for(lambda: (self.assertEqual(self.browser.find_element(by=By.CSS_SELECTOR, value='.has-error'),
                                                "You can't have an empty list item")))
        """empty list item She gets a similar warning on the list page 
        AND she can fix it by filling in the field with some text"""
        self.browser.find_element(by=By.ID, value='id_new_item').send_keys('Make tea')
        self.browser.find_element(by=By.ID, value='id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
        self.fail('Write on ME!')
