from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.Base_page import BasePage
import time  # Add this import


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.fname_input = (By.ID, "firstNameInput")
        self.lname_input = (By.ID, "lastNameInput")
        self.address_input = (By.ID, "addressLine1Input")
        self.state_input = (By.ID, "provinceInput")
        self.zip_input = (By.ID, "postCodeInput")
        self.submit_btn = (By.ID, "checkout-shipping-continue")
        self.success_msg = (By.ID, "confirmation-message")

    def enter_shipping_details(self, fname, lname, address, state, zipcode):
        self.log.info("--- Entering Shipping Details ---")


        self.log.info("Waiting 3 seconds for checkout page to render...")
        time.sleep(3)

        self.enter_text(self.fname_input, fname, "First Name")
        self.enter_text(self.lname_input, lname, "Last Name")
        self.enter_text(self.address_input, address, "Address")
        self.enter_text(self.state_input, state, "State/Province")
        self.enter_text(self.zip_input, zipcode, "Zip Code")
        self.click_element(self.submit_btn, "Submit Order Button")

    def verify_order_success(self):
        element = self.wait.until(EC.visibility_of_element_located(self.success_msg))
        return element.text