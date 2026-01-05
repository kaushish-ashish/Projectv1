import pytest
import allure

from pageObjects.HomePage import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_HomePageArrivals:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.feature("Home Page")
    @allure.story("Arrivals Count Validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_homepage_arrivals_count(self, setup):
        self.logger.info("**** Test_001_HomePageArrivals started ****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Launching application")

        home = HomePage(self.driver)

        self.logger.info("Clicking on Shop menu")
        home.clickShopMenu()

        self.logger.info("Clicking on Home menu")
        home.clickHomeMenu()

        self.logger.info("Validating number of Arrivals on Home page")
        arrivals_count = home.getArrivalsCount()

        try:
            assert arrivals_count == 3, \
                f"Expected 3 arrivals on Home page, but found {arrivals_count}"
            self.logger.info("Home page contains exactly 3 arrivals")

        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Arrivals_Count_Mismatch",
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error(
                f"Arrivals count validation failed. Found {arrivals_count}"
            )
            raise e

        self.logger.info("**** Test_001_HomePageArrivals finished ****")
