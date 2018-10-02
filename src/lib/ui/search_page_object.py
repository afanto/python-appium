from ..ui import MainPageObject


class SearchPageObject(MainPageObject):


    SEARCH_INIT_ELEMENT = "xpath://*[contains(@text, 'Search Wikipedia')]"

    def search_page_object(self, driver):
        super().driver = driver

    def init_search_input(self):
        self.wait_for_element_and_click(self.SEARCH_INIT_ELEMENT, "Can't find and click search init element", 5)