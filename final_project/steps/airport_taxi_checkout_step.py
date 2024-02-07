import time

from selenium.webdriver.support.select import Select

from final_project.pages.airport_taxi_page import AirportTaxiCheckoutPage
from final_project.steps.my_common_actions import MyCommonActions


class AirportTaxiCheckoutStep(MyCommonActions, AirportTaxiCheckoutPage):
    def enter_first_name(self, first_name):
        self.fill(self.FIRST_NAME, first_name)

    def get_first_name_value(self):
        return self.get_value_element(self.FIRST_NAME)

    def enter_last_name(self, last_name):
        self.fill(self.LAST_NAME, last_name)

    def get_last_name_value(self):
        return self.get_value_element(self.LAST_NAME)

    def enter_email(self, email):
        self.fill(self.EMAIL, email)

    def get_email_value(self):
        return self.get_value_element(self.EMAIL)

    def select_phone_code(self, code):
        code_select = Select(self.find(self.PHONE_CODE_SELECT))
        code_select.select_by_value(code)

    def get_phone_code_value(self):
        code_select = Select(self.find(self.PHONE_CODE_SELECT))
        return code_select.first_selected_option.text.split(" ")[1]

    def enter_phone_number(self, number):
        self.fill(self.PHONE_NUMBER, number)

    def get_phone_number_value(self):
        return self.get_value_element(self.PHONE_NUMBER)

    def enter_name(self, name):
        self.go_to_element(self.CHECKOUT_SUBMIT_BUTTON)
        self.driver.switch_to.frame(self.find(self.PAYMENT_IFRAME))
        self.find(self.NAME).send_keys(name)

    def get_name_value(self):
        return self.get_value_element(self.NAME)

    def enter_card_number(self, card_number):
        self.fill(self.CARD_NUMBER, card_number)

    def get_card_number_value(self):
        return self.get_value_element(self.CARD_NUMBER)

    def select_card_type(self):
        self.click(self.CARD_TYPE)
        self.click(self.MASTER_CARD)

    def get_card_type_value(self):
        return self.get_text(self.CARD_TYPE_VALUE)

    def enter_expiration_date(self, expiration_date):
        self.fill(self.EXPIRY_DATE, expiration_date)

    def get_expiration_date_value(self):
        return self.get_value_element(self.EXPIRY_DATE)

    def enter_cvc_number(self, cvc_number):
        self.fill(self.CVC, cvc_number)

    def get_cvc_number_value(self):
        return self.get_value_element(self.CVC)

    def book_and_pay_btn_is_clickable(self):
        self.driver.switch_to.default_content()
        return self.find(self.CHECKOUT_SUBMIT_BUTTON).is_enabled()