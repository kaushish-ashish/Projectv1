import pytest
import allure

from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_HomePageArrivalsDescription:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.feature("Home Page")
    @allure.story("Arrivals Description Validation")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_homepage_arrivals_description(self, setup):
        self.logger.info("**** Test_004_HomePageArrivalsDescription started ****")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("Launching application")

        self.home = HomePage(self.driver)

        # Step 3: Click Shop Menu
        self.logger.info("Clicking on Shop menu")
        self.home.clickShopMenu()

        # Step 4: Click Home Menu
        self.logger.info("Clicking on Home menu")
        self.home.clickHomeMenu()

        # Step 5 & 6: Verify Arrivals count
        self.logger.info("Validating number of Arrivals on Home page")
        arrivals_count = self.home.getArrivalsCount()
        assert arrivals_count == 3, f"Expected 3 arrivals but found {arrivals_count}"

        # Step 7: Click first Arrival image
        self.logger.info("Clicking on first Arrival image")
        self.home.clickArrivalByIndex(0)

        self.product = ProductPage(self.driver)

        try:
            # Step 8 & 9: Verify Add to Basket is displayed
            assert self.product.isAddToBasketDisplayed()
            self.logger.info("Navigated to product page successfully")

            # Step 10: Click Description tab
            self.logger.info("Clicking on Description tab")
            self.product.clickDescriptionTab()

            # Step 11: Verify Description content is displayed
            assert self.product.isDescriptionDisplayed()
            self.logger.info("Product description is displayed successfully")

        except Exception as e:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Arrival_Description_Test_Failed",
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error("Arrival description validation failed")
            raise e

        self.driver.close()
        self.logger.info("**** Test_004_HomePageArrivalsDescription finished ****")
