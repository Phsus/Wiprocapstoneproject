import pytest
from Pages.Login_page import LoginPage
from utilities.logger import get_logger


@pytest.mark.usefixtures("setup")
class TestNegativeLogin:
    def test_locked_user_login(self):
        log = get_logger()
        log.info("========== STARTING LOCKED USER LOGIN TEST ==========")

        self.driver.get("https://bstackdemo.com/")
        login_page = LoginPage(self.driver)

        login_page.login("locked_user", "testingisfun99")

        try:
            error_text = login_page.get_login_error()
            assert "Your account has been locked." in error_text
            log.info("========== LOCKED USER TEST PASSED ==========")
        except AssertionError as e:
            log.error("========== LOCKED USER TEST FAILED ==========")
            raise e