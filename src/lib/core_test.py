from unittest import TestCase
import os
from appium import webdriver
import warnings

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CoreTestCase(TestCase):

    APPIUM_URL = 'http://localhost:4723/wd/hub'

    def setUp(self):
        warnings.simplefilter('ignore')
        super().setUp()
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9',
            'avd': 'Nexus_5X_API_28_x86',
            'deviceName': 'Nexus_5X_API_28_x86',
            'app': PATH('/users/andreyfrantov/prog/python-appium/apks/org.wikipedia.apk'),
            'appPackage': 'org.wikipedia',
            'appActivity': '.main.MainActivity'
        }

        self.driver = webdriver.Remote(self.APPIUM_URL, desired_caps)

    def tearDown(self):
        self.driver.quit()
        super().tearDown()
