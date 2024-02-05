import time

import pytest
from final_project.data.AccountData import AccountData
from final_project.data.CommonData import Urls
from final_project.steps.SignInSteps import SignInSteps
from assertpy import assert_that, soft_assertions


class TestSignIn:
    def test_precondition(self, driver):
        rs = SignInSteps(driver)
        rs.open_page(Urls.HOME_URL)
        rs.driver.refresh()
        rs.open_sign_in()

    @pytest.mark.parametrize('email, expected', AccountData.sign_in_email_data)
    def test_email_validation(self, driver, email, expected):
        rs = SignInSteps(driver)
        rs.fill_email(email)
        with soft_assertions():
            assert_that(rs.submit_email()).contains(expected)

    @pytest.mark.parametrize('password, expected', AccountData.sign_in_password_data)
    def test_password_validation(self, driver, password, expected):
        rs = SignInSteps(driver)
        rs.fill_password(password)
        with soft_assertions():
            assert_that(rs.submit_password()).contains(expected)
