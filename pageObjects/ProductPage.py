import allure
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage


class ProductPage(BasePage):

    # ---------- Locators ----------
    BTN_ADD_TO_BASKET = (By.XPATH, "//button[text()='Add to basket']")
    DESCRIPTION_TAB = (By.XPATH, "//a[normalize-space()='Description']")
    DESCRIPTION_CONTENT = (By.ID, "tab-description")

    REVIEW_TAB = (By.XPATH, "//a[normalize-space()='Reviews (0)']")
    REVIEW_CONTENT = (By.ID, "comments")

    BTN_VIEW_BASKET = (By.XPATH, "//a[normalize-space()='View Basket']")
    BASKET_PRICE = (By.XPATH, "//span[@class='amount']")

    # ---------- Constructor ----------
    def __init__(self, driver):
        super().__init__(driver)

    # ---------- Add To Basket ----------
    @allure.step("Verify Add to Basket button is displayed")
    def isAddToBasketDisplayed(self):
        btn = self.wait_for_visibility(self.BTN_ADD_TO_BASKET)
        self.scroll_to_element(btn)
        return btn.is_displayed()

    @allure.step("Click on Add To Basket button")
    def clickAddToBasket(self):
        btn = self.wait_for_clickable(self.BTN_ADD_TO_BASKET)
        self.scroll_to_element(btn)
        btn.click()

    def ViewBasket(self):
        btn = self.wait_for_clickable(self.BTN_VIEW_BASKET)
        self.scroll_to_element(btn)
        btn.click()


    # @allure.step("Verify product is visible in basket menu")
    # def isBasketItemDisplayedInMenu(self):
    #     basket = self.wait_for_visibility(self.BASKET_MENU)
    #     return basket.is_displayed()
    #
    # @allure.step("Verify basket price is displayed")
    # def isBasketPriceDisplayed(self):
    #     price = self.wait_for_visibility(self.BASKET_PRICE)
    #     return price.is_displayed()

    # ---------- Description ----------
    @allure.step("Click on Description tab")
    def clickDescriptionTab(self):
        tab = self.wait_for_clickable(self.DESCRIPTION_TAB)
        self.scroll_to_element(tab)
        tab.click()

    @allure.step("Verify product description is displayed")
    def isDescriptionDisplayed(self):
        desc = self.wait_for_visibility(self.DESCRIPTION_CONTENT)
        self.scroll_to_element(desc)
        return desc.is_displayed()

    # ---------- Reviews ----------
    @allure.step("Click on Reviews tab")
    def clickReviewsTab(self):
        reviews_tab = self.wait_for_clickable(self.REVIEW_TAB)
        self.scroll_to_element(reviews_tab)
        reviews_tab.click()

    @allure.step("Verify reviews section is displayed")
    def isReviewsDisplayed(self):
        reviews = self.wait_for_visibility(self.REVIEW_CONTENT)
        self.scroll_to_element(reviews)
        return reviews.is_displayed()
