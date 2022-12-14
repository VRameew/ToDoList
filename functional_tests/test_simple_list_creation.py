from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


MAX_WAIT = 10


class NewVisitorTest(FunctionalTest):
    """Test with Django manegment"""

    def test_can_start_a_list_for_one_user(self):
        # Test is starting of list and showed it later
        self.browser.get(self.live_server_url)
        # She sees that the title and header of the page are talking about to-do lists.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(by=By.TAG_NAME, value='h1').text
        self.assertIn('To-Do', header_text)
        # She is immediately prompted to enter a list item.
        input_box = self.get_item_input_box()
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # She types in the text box "Buy peacock feathers"
        # (her hobby is tying fishing flies). When she presses enter,
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # the page refreshes and the page now contains
        # "1: Buy Peacock Feathers" as a list item.
        # The text box still prompts her to add another item.
        # She types "Make a fly out of peacock feathers"
        # (Edith is very methodical)
        input_box = self.get_item_input_box()
        input_box.send_keys('Make a fly out of peacock feathers')
        input_box.send_keys(Keys.ENTER)
        # The page refreshes again to show both items in her list.
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Make a fly out of peacock feathers')
        # Edith wonders if the site will remember her list.
        # Next, she sees that the site has generated a unique URL for her
        # - a small text with explanations is displayed about this.
        # She visits this URL - her list is still there.
        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """Many users can start a list Of To-Do"""
        # Edit start new list
        self.browser.get(self.live_server_url)
        input_box = self.get_item_input_box()
        input_box.send_keys('Buy peacock feathers')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        editth_list_url = self.browser.current_url
        self.assertRegex(editth_list_url, '/lists/.+')

        # Now a new user, Francis, is coming to the site.
        # We use a new browser session,
        # thereby ensuring that no information from Edith
        # gets passed through cookie data, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()
        # Francis visits the homepage. There is no sign of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(by=By.TAG_NAME, value='body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Make a fly out of peacock feathers', page_text)
        # Francis starts a new list by introducing a new element.
        # It's less interesting than Edith's list...
        input_box = self.get_item_input_box()
        input_box.send_keys('Buy milk')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        # Francis gets a unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, editth_list_url)

        page_text = self.browser.find_element(by=By.TAG_NAME, value='body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
