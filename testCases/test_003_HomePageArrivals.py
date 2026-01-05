import pytest
import os
import allure
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_HomePageArrivals:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.feature("Home Page")
    @allure.story("All Arrivals Navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_homepage_all_arrivals_navigation(self, setup):
        self.logger.info("**** Test_003_HomePageArrivals started ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.home = HomePage(self.driver)

        self.logger.info("Clicking on Shop menu")
        self.home.clickShopMenu()

        self.logger.info("Clicking on Home menu")
        self.home.clickHomeMenu()

        self.logger.info("Validating Arrivals count")
        arrivals_count = self.home.getArrivalsCount()
        assert arrivals_count == 3, f"Expected 3 arrivals, but found {arrivals_count}"

        self.logger.info("Clicking all Arrival images one by one")

        for index in range(arrivals_count):
            self.logger.info(f"Clicking Arrival image {index + 1}")
            self.home.clickArrivalByIndex(index)

            product_page = ProductPage(self.driver)

            try:
                assert product_page.isAddToBasketDisplayed()
                self.logger.info("Navigated to product page successfully")
            except Exception as e:
                allure.attach(
                    self.driver.get_screenshot_as_png(),
                    name=f"Arrival_{index + 1}_Navigation_Failed",
                    attachment_type=allure.attachment_type.PNG
                )
                self.logger.error("Arrival image navigation failed")
                raise e

            self.logger.info("Navigating back to Home page")
            self.driver.back()

        self.driver.close()
        self.logger.info("**** Test_003_HomePageArrivals finished ****")
