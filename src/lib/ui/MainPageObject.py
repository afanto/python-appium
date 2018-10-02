from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPageObject():

    def main_page_object(self, driver):
        self.driver = driver

    def wait_for_element_present(self, locator, error_message, timeout_seconds=5):
        by = self.get_locator_by_string(locator)
        wait = WebDriverWait(self.driver, timeout_seconds)
        return wait.until(EC.presence_of_element_located(by), error_message + "\n")

    def wait_for_element_and_click(self, locator, error_message, timeout_seconds):
        element = self.wait_for_element_present(locator, error_message, timeout_seconds)
        element.click()
        return element

    def wait_for_element_and_send_keys(self, locator, value, error_message, timeout_seconds):
        element = self.wait_for_element_present(locator, error_message, timeout_seconds)
        element.send_keys(value)
        return element

    def get_locator_by_string(self, locator_with_type):
        exploded_locator = locator_with_type.split(":", 2)
        by_type = exploded_locator[0]
        locator = exploded_locator[1]

        if by_type.equals("xpath"):
            by = (By.XPATH, locator)
            return by
        elif by_type.equals("id"):
            by = (By.ID, locator)
            return by
        elif by_type.equals("css"):
            by = (By.CSS_SELECTOR, locator)
            return by
        else:
            raise Exception("Cannot get type of locator. Locator: " + locator_with_type)


