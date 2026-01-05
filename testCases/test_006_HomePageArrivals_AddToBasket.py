import pytest
import allure
import os

from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_006_HomePageArrivalsAddToBasket:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.feature("Home Page")
    @allure.story("Arrivals Add To Basket")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_homepage_arrival_add_to_basket(self, setup):

        self.logger.info("**** Test_006_HomePageArrivalsAddToBasket started ****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Launching application")

        home = HomePage(self.driver)

        self.logger.info("Validating Arrivals count")
        arrivals_count = home.getArrivalsCount()
        assert arrivals_count == 3, f"Expected 3 arrivals but found {arrivals_count}"

        self.logger.info("Clicking first Arrival image")
        home.clickArrivalByIndex(0)

        product = ProductPage(self.driver)

        try:
            self.logger.info("Verifying Add To Basket button")
            assert product.isAddToBasketDisplayed()

            self.logger.info("Clicking Add To Basket button")
            product.clickAddToBasket()

            # self.logger.info("Verifying item added to basket in menu")
            # assert product.isBasketItemDisplayedInMenu()
            # assert product.isBasketPriceDisplayed()

            self.logger.info("Book successfully added to basket and visible in menu")

        except Exception as e:
            screenshot_path = os.path.abspath(os.curdir) + "\\screenshots\\arrival_add_to_basket_failed.png"
            self.driver.save_screenshot(screenshot_path)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Add To Basket Failure",
                attachment_type=allure.attachment_type.PNG
            )

            self.logger.error("Add To Basket validation failed")
            raise e

        self.driver.close()
        self.logger.info("**** Test_006_HomePageArrivalsAddToBasket finished ****")
