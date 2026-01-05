import pytest
import allure
import os

from pageObjects.HomePage import HomePage
from pageObjects.ProductPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_005_HomePageArrivalsReviews:

    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()

    @allure.feature("Home Page")
    @allure.story("Arrivals Reviews Validation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_homepage_arrival_reviews(self, setup):

        self.logger.info("**** Test_005_HomePageArrivalsReviews started ****")

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
            self.logger.info("Clicking on Reviews tab")
            product.clickReviewsTab()

            self.logger.info("Verifying Reviews section")
            assert product.isReviewsDisplayed()

            self.logger.info("Reviews tab validation successful")

        except Exception as e:
            screenshot_path = os.path.abspath(os.curdir) + "\\screenshots\\arrival_reviews_failed.png"
            self.driver.save_screenshot(screenshot_path)

            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Arrival Reviews Failure",
                attachment_type=allure.attachment_type.PNG
            )

            self.logger.error("Arrival Reviews validation failed")
            raise e

        self.driver.close()
        self.logger.info("**** Test_005_HomePageArrivalsReviews finished ****")
