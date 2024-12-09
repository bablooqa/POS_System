import pytest
from selenium import webdriver
import os.path
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

## Setup chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless") # Ensure GUI is off
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--disable-dev-shm-usage')

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        
        
        # driver = webdriver.Chrome()
        # link = "https://accounts.google.com"
        driver = webdriver.Chrome(executable_path=r"B:\ZapBuild-Work\bottlepos5-qa-main\chromeDriver/chromedriver.exe")
        print("Launching Chrome browser....")
        # driver.get(link)
        # homedir = os.path.expanduser("~")
        # webdriver_service = Service(f"{homedir}/chromeDriver/chromedriver")
    elif browser == "firefox":
        # driver = webdriver.Firefox()
        driver = webdriver.Firefox(executable_path=r"B:\ZapBuild-Work\bottlepos5-qa-main\chromeDriver/chromedriver.exe")
 
        print("  Launching Firefox browser....")
    else:
        # driver = webdriver.Edge()
        driver = webdriver.Edge(
            executable_path=r"B:\ZapBuild-Work\bottlepos5-qa-main\chromeDriver/chromedriver.exe")
        print("Launching IE browser....")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")


@pytest.fixture  
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# ------------------------Generate PyTest HTML Report----------------------#

# This is hook for additing Environment info to HTML Report

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Bottlepos 3.0'
#     config._metadata['Module Name'] = 'Item'
#     config._metadata['Tester'] = 'Onkar Singh'


# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugin", None)
