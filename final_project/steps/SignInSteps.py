import time

from selenium.webdriver import Keys
from final_project.pages.SignInPage import SignInPage as sp
from final_project.pages.CommopPage import CommonPage as cp
from final_project.steps.common_actions import Common


class SignInSteps(Common):

    def open_sign_in(self):
        self.click(cp.SIGN_IN)

    def fill_email(self, email: str):
        elem = self.find(sp.EMAIL_INPUT)
        elem.click()
        elem.clear()
        t = elem.text
        time.sleep(1)
        if not t == '':
            elem.send_keys(Keys.CONTROL + 'A')
        time.sleep(1)
        elem.send_keys(email)

    def get_email_error_note(self) -> str:
        return self.get_text(sp.ERROR_NOTE)

    def submit_email(self) -> str:
        self.wait_for(sp.EMAIL_INPUT).submit()
        try:
            return self.get_email_error_note()
        except:
            return 'Success'

    def fill_password(self, password):
        elem = self.wait_for(sp.PASSWORD)
        elem.click()
        elem.clear()
        t = elem.text
        time.sleep(1)
        if not t == '':
            elem.send_keys(Keys.CONTROL + 'A')
        time.sleep(1)
        elem.send_keys(password)

    def submit_password(self) -> str:
        self.find(sp.SUBMIT_SIGN_IN).submit()
        try:
            return self.get_password_error_note()
        except:
            return 'Success'

    def get_password_error_note(self) -> str:
        return self.get_text(sp.PASSWORD_NOTE)
