from .main_page_object import MainPageObject


class SearchPageObject(MainPageObject):

    SEARCH_INIT_ELEMENT = "xpath://*[contains(@text, 'Search Wikipedia')]"
    SEARCH_FIELD = "xpath://*[contains(@text, 'Search…')]"
    SEARCH_RESULT = "xpath://*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Object-oriented programming language']"

    def __init__(self, driver):
        super().__init__(driver)

    def init_search_input(self):
        self.wait_for_element_and_click(self.SEARCH_INIT_ELEMENT, "Can't find and click search init element", 5)