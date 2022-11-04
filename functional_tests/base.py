from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time
import os

MAX_WAIT = 10


class  FunctionalTest(StaticLiveServerTestCase):
    """FuncTest"""
    def setUp(self):
        """initialize"""
        self.browser = webdriver.Firefox()
        starting_server = os.environ.get('STAGING_SERVER')
        if starting_server:
            self.live_server_url =  'http://' + starting_server

    def tearDown(self):
        """finalize"""
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        """wait string in table rows"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(by=By.ID, value='id_list_table')
                rows = table.find_elements(by=By.TAG_NAME, value='tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)