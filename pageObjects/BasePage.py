from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ------------------ WAIT UTILITIES ------------------

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # ------------------ ACTION UTILITIES ------------------

    # def safe_click(self, locator):
    #     element = self.wait_for_clickable(locator)
    #     self.scroll_to_element(element)
    #     element.click()

    def safe_send_keys(self, locator, value, clear=True):
        element = self.wait_for_visibility(locator)
        self.scroll_to_element(element)
        if clear:
            element.clear()
        element.send_keys(value)

    def is_element_displayed(self, locator):
        try:
            return self.wait_for_visibility(locator).is_displayed()
        except TimeoutException:
            return False

    # ------------------ SCROLL UTILITIES ------------------

    def scroll_to_element(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )

    def scroll_by_pixels(self, x=0, y=500):
        self.driver.execute_script(f"window.scrollBy({x},{y});")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
