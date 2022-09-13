from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Test new user"""

    def setUp(self):
        """initialize"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """finalize"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Test is starting of list and showed it later"""
        self.browser.get('http://localhost:8000')
        """She sees that the title and header of the page are talking about to-do lists."""
        self.assertIn('To-Do', self.browser.title)
        self.fail('End of test!')
    """She is immediately prompted to enter a list item.
        She types in the text box "Buy peacock feathers"
        (her hobby is tying fishing flies). When she presses enter,
        the page refreshes and the page now contains 
        "1: Buy Peacock Feathers" as a list item. 
        The text box still prompts her to add another item. 
        She types "Make a fly out of peacock feathers"
        (Edith is very methodical)
        The page refreshes again to show both items in her list. 
        Edith wonders if the site will remember her list. 
        Next, she sees that the site has generated a unique URL for her 
        - a small text with explanations is displayed about this. 
        She visits this URL - her list is still there. 
        Satisfied, she goes back to sleep"""


if __name__ == '__main__':
    unittest.main(warnings='ignore')
