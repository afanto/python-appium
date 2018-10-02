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
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['avd'] = 'Nexus_5X_API_28_x86'
        desired_caps['deviceName'] = 'Nexus_5X_API_28_x86'
        desired_caps['app'] = PATH(
            '/users/andreyfrantov/prog/python-appium/apks/org.wikipedia.apk'
        )
        desired_caps['appPackage'] = 'org.wikipedia'
        desired_caps['appActivity'] = '.main.MainActivity'

        self.driver = webdriver.Remote(self.APPIUM_URL, desired_caps)

    def tearDown(self):
        self.driver.quit()
        super().tearDown()
