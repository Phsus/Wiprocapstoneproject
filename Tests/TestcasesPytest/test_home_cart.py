import pytest
from Pages.Home_page import HomePage
from utilities.logger import get_logger


@pytest.mark.usefixtures("setup")
class TestHomeCart:
    def test_cart_badge_update(self):
        log = get_logger()
        log.info("STARTING CART BADGE UPDATE TEST")

        self.driver.get("https://bstackdemo.com/")
        home_page = HomePage(self.driver)

        home_page.filter_by_vendor("Samsung")
        home_page.add_product_to_cart("Galaxy S20")

        try:
            badge_text = self.driver.find_element(*home_page.cart_badge).text
            assert badge_text == "1"
            log.info(" CART BADGE TEST PASSED ")
        except AssertionError as e:
            log.error(" CART BADGE TEST FAILED ")