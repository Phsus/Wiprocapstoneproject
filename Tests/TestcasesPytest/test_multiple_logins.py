import pytest
from Pages.Login_page import LoginPage
from Pages.Home_page import HomePage
from utilities.logger import get_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestMultipleLogins:

    @pytest.mark.parametrize("test_user", [
        "image_not_loading_user",
        "existing_orders_user",
        "fav_user"
    ])
    def test_valid_logins(self, test_user):
        log = get_logger()
        log.info(f"========== TESTING LOGIN FOR: {test_user} ==========")


        self.driver.get("https://bstackdemo.com/")


        self.driver.delete_all_cookies()
        self.driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")


        self.driver.get("https://bstackdemo.com/")

        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)


        login_page.login(test_user, "testingisfun99")

        try:

            username_locator = (By.CLASS_NAME, "username")
            home_page.wait.until(EC.visibility_of_element_located(username_locator))
            log.info(f"========== {test_user} LOGIN PASSED ==========")

        except Exception as e:
            log.error(f"========== {test_user} LOGIN FAILED: {str(e)} ==========")
            raise e