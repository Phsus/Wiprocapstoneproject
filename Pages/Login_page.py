from selenium.webdriver.common.by import By
from Pages.Base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.signin_link = (By.ID, "signin")


        self.username_dropdown = (By.CSS_SELECTOR, "#username input")
        self.password_dropdown = (By.CSS_SELECTOR, "#password input")

        self.login_btn = (By.ID, "login-btn")
        self.error_message = (By.CLASS_NAME, "api-error")

    def login(self, username, password):
        self.log.info(f"--- Starting Login Process for user: {username} ---")
        self.click_element(self.signin_link, "Sign In Link")

        self.enter_text(self.username_dropdown, username + "\n", "Username Dropdown")
        self.enter_text(self.password_dropdown, password + "\n", "Password Dropdown")

        self.click_element(self.login_btn, "Login Button")

    def get_login_error(self):
        from selenium.webdriver.support import expected_conditions as EC
        element = self.wait.until(EC.visibility_of_element_located(self.error_message))
        self.log.info(f"Captured error message: {element.text}")
        return element.text