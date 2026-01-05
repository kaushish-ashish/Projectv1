import allure
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class HomePage(BasePage):

    # ---------- Locators ----------
    MENU_SHOP = (By.XPATH, "//a[text()='Shop']")
    MENU_HOME = (By.XPATH, "//a[text()='Home']")
    ARRIVALS = (By.XPATH, "//div[@class='woocommerce']//ul[@class='products']/li")
    ARRIVALS_IMAGES = (By.XPATH, "//div[@class='woocommerce']//ul[@class='products']/li/a[1]")

    def __init__(self, driver):
        super().__init__(driver)

    # ---------- Actions ----------
    @allure.step("Click on Shop menu")
    def clickShopMenu(self):
        self.wait_for_clickable(self.MENU_SHOP).click()

    @allure.step("Click on Home menu")
    def clickHomeMenu(self):
        self.wait_for_clickable(self.MENU_HOME).click()

    # ---------- Validations ----------
    @allure.step("Get number of Arrivals on Home page")
    def getArrivalsCount(self):
        arrivals = self.wait.until(
            lambda d: d.find_elements(*self.ARRIVALS)
        )
        return len(arrivals)

    @allure.step("Get all Arrival images")
    def getArrivalImages(self):
        return self.wait.until(
            lambda d: d.find_elements(*self.ARRIVALS_IMAGES)
        )

    @allure.step("Click Arrival image at index: {index}")
    def clickArrivalByIndex(self, index):
        arrivals = self.getArrivalImages()

        if index >= len(arrivals):
            raise IndexError("Arrival index out of range")

        arrival = arrivals[index]
        self.scroll_to_element(arrival)
        arrival.click()
