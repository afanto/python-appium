import os
import pytest
from appium import webdriver


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)

@pytest.fixture
def driver_setup(request):
    capabilities = {}
    capabilities['platformName'] = 'Android'
    capabilities['platformVersion'] = '9'
    capabilities['deviceName'] = 'Android Emulator'
    capabilities['app'] = PATH('/users/andreyfrantov/prog/PythonAppiumAutomation/apks/org.wikipedia.apk')
    capabilities['appPackage'] = 'org.wikipedia'
    capabilities['appActivity'] = '.main.MainActivity'
    url = 'http://localhost:4723/wd/hub'
    request.instance.driver = webdriver.Remote(url, capabilities)

    def teardown():
        request.instance.driver.quit()

    request.addfinalizer(teardown)


def test_something(driver_setup):
    print("Hello World!")