from selenium.webdriver import Keys
from final_project.pages.RegistrationPage import RegistrationPage as rp
from final_project.pages.CommopPage import CommonPage as cp
from final_project.steps.common_actions import Common


class RegistrationSteps(Common):
    def open_registration(self):
        self.click(cp.REGISTER)

    def fill_email(self, email: str):
        elem = self.find(rp.EMAIL_INPUT)
        elem.click()
        elem.send_keys(Keys.CONTROL + 'A' + Keys.DELETE)
        if elem.text != '':
            elem.send_keys(Keys.CONTROL + 'A' + Keys.DELETE)
        if elem.text == 'A':
            elem.send_keys(Keys.BACKSPACE)
        elem.clear()
        elem.send_keys(email)

    def get_email_error_note(self) -> str:
        return self.get_text(rp.ERROR_NOTE)

    def submit_email(self) -> str:
        self.wait_for(rp.EMAIL_INPUT).submit()
        try:
            return self.get_email_error_note()
        except:
            return 'Success'

    def fill_new_password(self, password):
        elem = self.wait_for(rp.NEW_PASSWORD)
        elem.click()
        elem.send_keys(Keys.CONTROL + 'A' + Keys.DELETE)
        if elem.text != '':
            elem.send_keys(Keys.CONTROL + 'A' + Keys.DELETE)
        if elem.text == 'A':
            elem.send_keys(Keys.BACKSPACE)
        elem.clear()
        elem.send_keys(password)

    def confirm_password(self, password):
        elem = self.wait_for(rp.CONFIRM_PASSWORD)
        elem.click()
        elem.send_keys(Keys.CONTROL + 'A' + Keys.DELETE)
        if elem.text != '':
            elem.send_keys(Keys.CONTROL + 'A' + Keys.DELETE)
        if elem.text == 'A':
            elem.send_keys(Keys.BACKSPACE)
        elem.clear()
        elem.send_keys(password)

    def submit_password(self) -> str:
        self.find(rp.SUBMIT_REGISTER).submit()
        try:
            return self.get_password_error_note()
        except:
            return 'Success'

    def get_password_error_note(self) -> str:
        result = ''

        try:
            result += self.get_text(rp.NEW_PASSWORD_NOTE)
        except:
            pass
        try:
            result += self.get_text(rp.CONFIRM_PASSWORD_NOTE)
        except:
            pass

        if result == '':
            raise AssertionError

        return result
