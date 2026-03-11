from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.logger import get_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.log = get_logger()

    def click_element(self, locator, locator_name):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.log.info(f"Clicked on: {locator_name}")
        except TimeoutException as e:
            self.log.error(f"Failed to click on '{locator_name}'. Exception: {str(e)}")
            raise e

    def enter_text(self, locator, text, locator_name):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.log.info(f"Entered '{text}' into: {locator_name}")
        except TimeoutException as e:
            self.log.error(f"Failed to enter text in '{locator_name}'. Exception: {str(e)}")
            raise e