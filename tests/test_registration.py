from final_project.data.AccountData import AccountData
from final_project.steps.RegistrationSteps import RegistrationSteps
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions


class TestRegistration:
    def test_precondition(self, driver):
        rs = RegistrationSteps(driver)
        rs.open_page(Urls.HOME_URL)
        rs.driver.refresh()
        rs.open_registration()

    @pytest.mark.parametrize('email, expected', AccountData.email_data)
    def test_email_validation(self, driver, email, expected):
        rs = RegistrationSteps(driver)
        rs.fill_email(email)
        with soft_assertions():
            assert_that(rs.submit_email()).contains(expected)

    @pytest.mark.parametrize('password, confirm, expected', AccountData.password_confirm_data)
    def test_password_validation(self, driver, password, confirm, expected):
        rs = RegistrationSteps(driver)
        rs.fill_new_password(password)
        rs.confirm_password(confirm)
        with soft_assertions():
            assert_that(rs.submit_password()).contains(expected)
