from ..core_test import CoreTestCase
from ..ui import SearchPageObject
import os

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WikipediaTests(CoreTestCase):

    #INIT_SEARCH = "//*[contains(@text, 'Search Wikipedia')]"
    #SEARCH_FIELD = "//*[contains(@text, 'Search…')]"
    #SEARCH_RESULT = "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Object-oriented programming language']"

    def test_init_search(self):
        search_page_object = SearchPageObject()
        search_page_object.init_search_input()



"""
    def test_first(self):
        self.wait_for_element_by_xpath_and_click(
            self.INIT_SEARCH,
            "Cannot find Search Wikipedia input",
            10
        )

        self.wait_for_element_by_xpath_and_send_keys(
            self.SEARCH_FIELD,
            "Java",
            "Cannot find search input",
            5
        )

        self.wait_for_element_present_by_xpath(
            self.SEARCH_RESULT,
            "Cannot find 'Object-oriented programming language"
        )

    def wait_for_element_by_xpath_and_click(self, xpath, error_message, timeout_seconds):
        element = self.wait_for_element_present_by_xpath(xpath, error_message, timeout_seconds)
        element.click()
        return element

    def wait_for_element_present_by_xpath(self, xpath, error_message, timeout_seconds=5):
        wait = WebDriverWait(self.driver, timeout_seconds)
        by = (By.XPATH, xpath)
        return wait.until(EC.presence_of_element_located(by), error_message + "\n")

    def wait_for_element_by_xpath_and_send_keys(self, xpath, value, error_message, timeout_seconds):
        element = self.wait_for_element_present_by_xpath(xpath, error_message, timeout_seconds)
        element.send_keys(value)
        return element
"""