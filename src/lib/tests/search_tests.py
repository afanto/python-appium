from ..core_test import CoreTestCase
from ..ui import SearchPageObject
import os


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class WikipediaTests(CoreTestCase):

    def test_init_search(self):
        search_page_object = SearchPageObject(self.driver)
        search_page_object.init_search_input()
