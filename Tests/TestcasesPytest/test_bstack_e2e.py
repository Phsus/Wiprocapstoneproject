import pytest
from Pages.Login_page import LoginPage
from Pages.Home_page import HomePage
from Pages.Checkout_page import CheckoutPage
from utilities.excel_reader import get_test_data
from utilities.logger import get_logger


@pytest.mark.usefixtures("setup")
class TestBstackDemo:

    def test_end_to_end_checkout(self):
        log = get_logger()
        log.info("========== STARTING E2E CHECKOUT TEST ==========")

        # 1. Fetch Data from Excel
        data = get_test_data("testdata/testdata.xlsx")
        username, password, product, fname, lname, address, state, zipcode = data

        self.driver.get("https://bstackdemo.com/")

        # 2. Initialize Page Objects
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        # 3. Execute Automation Flow
        login_page.login(username, password)


        # Since we are buying an iPhone 12, we filter the page by 'Apple'
        home_page.filter_by_vendor("Apple")

        home_page.add_product_to_cart(product)
        home_page.proceed_to_checkout()

        checkout_page.enter_shipping_details(fname, lname, address, state, str(zipcode))

        # 4. Final Validation
        try:
            confirmation = checkout_page.verify_order_success()
            assert "Your Order has been successfully placed" in confirmation
            log.info("========== TEST PASSED SUCCESSFULLY ==========")
        except AssertionError as e:
            log.error("========== TEST FAILED: Assertion Error ==========")
            raise e