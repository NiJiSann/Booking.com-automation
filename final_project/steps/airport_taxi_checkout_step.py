import time
import allure
from selenium.webdriver.support.select import Select
from final_project.pages.airport_taxi_page import AirportTaxiCheckoutPage
from final_project.steps.my_common_actions import MyCommonActions


class AirportTaxiCheckoutStep(MyCommonActions, AirportTaxiCheckoutPage):

    @allure.step("Assert that airport taxi checkout page is opened")
    def taxi_checkout_page_is_opened(self):
        return self.find(self.TAXI_CHECKOUT_TITLE).is_displayed()

    @allure.step("Fill first name: {first_name}")
    def enter_first_name(self, first_name):
        self.fill(self.FIRST_NAME, first_name)

    @allure.step("Assert that first name is filled")
    def get_first_name_value(self):
        return self.get_value_element(self.FIRST_NAME)

    @allure.step("Fill last name: {last_name}")
    def enter_last_name(self, last_name):
        self.fill(self.LAST_NAME, last_name)

    @allure.step("Assert that last name is filled")
    def get_last_name_value(self):
        return self.get_value_element(self.LAST_NAME)

    @allure.step("Fill email: {email}")
    def enter_email(self, email):
        self.fill(self.EMAIL, email)

    @allure.step("Assert that email is filled")
    def get_email_value(self):
        return self.get_value_element(self.EMAIL)

    @allure.step("Select phone code: {code}")
    def select_phone_code(self, code):
        code_select = Select(self.find(self.PHONE_CODE_SELECT))
        code_select.select_by_value(code)

    @allure.step("Assert that phone code is selected")
    def get_phone_code_value(self):
        code_select = Select(self.find(self.PHONE_CODE_SELECT))
        return code_select.first_selected_option.text.split(" ")[1]

    @allure.step("Fill phone number: {number}")
    def enter_phone_number(self, number):
        self.fill(self.PHONE_NUMBER, number)

    @allure.step("Assert that phone number is filled")
    def get_phone_number_value(self):
        return self.get_value_element(self.PHONE_NUMBER)

    @allure.step("Fill cardholder's name: {name}")
    def enter_name(self, name):
        self.go_to_element(self.CHECKOUT_SUBMIT_BUTTON)
        self.driver.switch_to.frame(self.find(self.PAYMENT_IFRAME))
        self.find(self.NAME).send_keys(name)

    @allure.step("Assert that card holder's name is filled")
    def get_name_value(self):
        return self.get_value_element(self.NAME)

    @allure.step("Fill card number: {card_number}")
    def enter_card_number(self, card_number):
        self.fill(self.CARD_NUMBER, card_number)

    @allure.step("Assert that card number is filled")
    def get_card_number_value(self):
        return self.get_value_element(self.CARD_NUMBER)

    @allure.step("Select card type: {card_type}")
    def select_card_type(self, card_type):
        self.click(self.CARD_TYPE)
        self.js_click(self.MASTER_CARD)

    @allure.step("Assert that card type is selected")
    def get_card_type_value(self):
        time.sleep(10)
        return self.get_text(self.CARD_TYPE_VALUE)

    @allure.step("Fill expiry date: {expiration_date}")
    def enter_expiration_date(self, expiration_date):
        self.fill(self.EXPIRY_DATE, expiration_date)

    @allure.step("Assert that expiry date is filled")
    def get_expiration_date_value(self):
        return self.get_value_element(self.EXPIRY_DATE)

    @allure.step("Fill cvc card number: {cvc_number}")
    def enter_cvc_number(self, cvc_number):
        self.fill(self.CVC, cvc_number)

    @allure.step("Assert that cvc number is filled")
    def get_cvc_number_value(self):
        return self.get_value_element(self.CVC)

    @allure.step("Assert that 'Book and Pay' button is clickable")
    def book_and_pay_btn_is_clickable(self):
        self.driver.switch_to.default_content()
        return self.find(self.CHECKOUT_SUBMIT_BUTTON).is_enabled()