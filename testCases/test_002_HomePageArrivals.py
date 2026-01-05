import pytest
import allure
from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_HomePageArrivals:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.feature("Home Page")
    @allure.story("Single Arrival Navigation")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression
    def test_homepage_arrival_navigation(self, setup):
        self.logger.info("**** Test_002_HomePageArrivals started ****")
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
        assert arrivals_count == 3, f"Expected 3 arrivals, but found {arrivals_count}"

        self.logger.info("Clicking on first Arrival image")
        home.clickArrivalByIndex(0)

        product_page = ProductPage(self.driver)

        try:
            assert product_page.isAddToBasketDisplayed(), \
                "Add to Basket button not visible on product page"
            self.logger.info("Arrival image navigated successfully to product page")

        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="First_Arrival_Navigation_Failed",
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error("Arrival image navigation failed")
            raise e

        self.logger.info("**** Test_002_HomePageArrivals finished ****")
