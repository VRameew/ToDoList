from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import unittest
import time


class NewVisitorTest(LiveServerTestCase):
    """Test with Django manegment"""

    def setUp(self):
        """initialize"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """finalize"""
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        """verification string in table rows"""
        table = self.browser.find_element(by=By.ID, value='id_list_table')
        rows = table.find_elements(by=By.TAG_NAME, value='tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Test is starting of list and showed it later
        self.browser.get(self.live_server_url)
        # She sees that the title and header of the page are talking about to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(by=By.TAG_NAME, value='h1').text
        self.assertIn('To-Do', header_text)
        # She is immediately prompted to enter a list item.
        input_box = self.browser.find_element(by=By.ID, value='id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types in the text box "Buy peacock feathers"
        # (her hobby is tying fishing flies). When she presses enter,
        time.sleep(1)
        input_box.send_keys('Buy peacock feathers')
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # the page refreshes and the page now contains
        # "1: Buy Peacock Feathers" as a list item.
        # The text box still prompts her to add another item.
        # She types "Make a fly out of peacock feathers"
        # (Edith is very methodical)
        input_box = self.browser.find_element(by=By.ID, value='id_new_item')
        time.sleep(1)
        input_box.send_keys('Make a fly out of peacock feathers')
        time.sleep(1)
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)
        # The page refreshes again to show both items in her list.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Make a fly out of peacock feathers')
        # Edith wonders if the site will remember her list.
        # Next, she sees that the site has generated a unique URL for her
        # - a small text with explanations is displayed about this.
        # She visits this URL - her list is still there.
        # Satisfied, she goes back to sleep
        self.fail('End of test!')
