from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import BasePage
import time


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = (By.CLASS_NAME, "buy-btn")
        self.cart_badge = (By.CLASS_NAME, "bag__quantity")
        self.logout_btn = (By.ID, "logout")  # The ID on bstackdemo
        self.user_display = (By.CLASS_NAME, "username")

    def filter_by_vendor(self, vendor_name):
        self.log.info(f"--- Filtering products by Vendor: {vendor_name} ---")
        vendor_checkbox = (By.XPATH, f"//span[text()='{vendor_name}']")
        self.click_element(vendor_checkbox, f"Vendor Filter: {vendor_name}")
        time.sleep(1)

    def add_product_to_cart(self, product_name):
        self.log.info(f"--- Selecting Product: {product_name} ---")
        product_xpath = (By.XPATH, f"//p[text()='{product_name}']/parent::div//div[text()='Add to cart']")
        self.click_element(product_xpath, f"Add to Cart: {product_name}")
        self.wait.until(EC.text_to_be_present_in_element(self.cart_badge, "1"))
        self.log.info("Cart updated successfully!")

    def proceed_to_checkout(self):
        time.sleep(2)
        self.click_element(self.checkout_btn, "Slide-out Cart Checkout Button")


    def logout(self):
        self.log.info("Attempting to logout...")
        try:

            logout_el = self.wait.until(EC.presence_of_element_located(self.logout_btn))


            self.driver.execute_script("arguments[0].click();", logout_el)


            signin_link = (By.ID, "signin")
            self.wait.until(EC.presence_of_element_located(signin_link))
            self.log.info("Logout successful!")
        except Exception as e:
            self.log.error(f"Logout failed! Error: {str(e)}")

            self.driver.refresh()
            raise e