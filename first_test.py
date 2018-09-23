import unittest
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class WikipediaTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '/users/andreyfrantov/prog/python_appium/apks/org.wikipedia.apk'
        )
        desired_caps['appPackage'] = 'org.wikipedia'
        desired_caps['appActivity'] = '.main.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
            self.driver.quit()

    def test_1(self):
        waitForElementByXpathAndClick(
            "//*[contains(@text, 'Search Wikipedia')]",
            "Cannot find Search Wikipedia input",
            5
        )
        waitForElementByXpathAndSendKeys(
            "//*[contains(@text, 'Search…')]",
            "Java",
            "Cannot find search input",
            5
        )
        wait_for_element_present_by_xpath(
            "//*[@resource-id='org.wikipedia:id/page_list_item_container']//*[@text='Object-oriented programming language']",
            "Cannot find 'Object-oriented programming language", 5)

    def wait_for_element_present_by_xpath(self, xpath, error_message, timeout_in_seconds):
        wait = WebDriverWait(self.driver, timeout_in_seconds)
        wait.withMessage(error_message + "\n")
        by = By.xpath(xpath)
        return wait.until(EC.presenceOfElementLocated(by))

    def wait_for_element_present_by_xpath(self, xpath, error_message):
        return wait_for_element_present_by_xpath(xpath, error_message)

