from datetime import datetime

import pytest
import os
import allure
from allure_commons.types import AttachmentType

from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# ---------- Add CLI option ----------
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


# ---------- Browser fixture ----------
@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-notifications")

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options
        )
        print("Launching Edge browser")

    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("dom.webnotifications.enabled", False)

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=firefox_options
        )
        print("Launching Firefox browser")

    else:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )
        print("Launching Chrome browser")

    driver.maximize_window()
    yield driver
    driver.quit()

# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
#
# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Opencart'
#     config._metadata['Module Name'] = 'CustRegistration'
#     config._metadata['Tester'] = 'Pavan'
#
# #Specifying report folder location and save report with timestamp
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"


# ---------- Allure Screenshot on Failure ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only if test failed during execution
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{test_name}_{timestamp}.png"
            )

            driver.save_screenshot(screenshot_path)

            print(f"\n Screenshot saved at: {screenshot_path}")

def pytest_sessionstart(session):
    with open("allure-results/environment.properties", "w") as f:
            f.write("Browser=Chrome\n")
            f.write("OS=Windows\n")
            f.write("BaseURL=https://practice.automationtesting.in\n")
            f.write("Execution=Local\n")
            f.write("Tester=Ashish Kumar\n")
