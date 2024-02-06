import allure
from final_project.data.AccountData import AccountData
from final_project.steps.RegistrationSteps import RegistrationSteps
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
from API.GSpread.allure_report_texts import Table as report_text_sheet


@allure.feature(report_text_sheet.get_value('additional'))
class TestRegistration:
    @allure.title('')
    @allure.description('')
    def test_precondition(self, driver):
        rs = RegistrationSteps(driver)
        with allure.step(''):
            rs.open_page(Urls.HOME_URL)
        with allure.step(''):
            rs.driver.refresh()
        with allure.step(''):
            rs.open_registration()

    @pytest.mark.parametrize('email, expected', AccountData.email_data)
    @allure.title('')
    @allure.description('')
    def test_email_validation(self, driver, email, expected):
        rs = RegistrationSteps(driver)
        with allure.step(''):
            rs.fill_email(email)
        with soft_assertions(), allure.step(''):
            assert_that(rs.submit_email()).contains(expected)

    @pytest.mark.parametrize('password, confirm, expected', AccountData.password_confirm_data)
    @allure.title('')
    @allure.description('')
    def test_password_validation(self, driver, password, confirm, expected):
        rs = RegistrationSteps(driver)
        with allure.step(''):
            rs.fill_new_password(password)
        with allure.step(''):
            rs.confirm_password(confirm)
        with soft_assertions(), allure.step(''):
            assert_that(rs.submit_password()).contains(expected)
