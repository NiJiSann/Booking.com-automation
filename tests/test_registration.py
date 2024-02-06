import allure
from final_project.data.AccountData import AccountData
from final_project.steps.RegistrationSteps import RegistrationSteps
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
from API.GSpread.allure_report_texts import Table as report_text_sheet


@allure.feature(report_text_sheet.get_value('additional'))
class TestRegistration:
    @allure.title(report_text_sheet.get_value('register_preconditions_title'))
    @allure.description(report_text_sheet.get_value('register_preconditions_desc'))
    def test_precondition(self, driver):
        rs = RegistrationSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            rs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            rs.driver.refresh()
        with allure.step(report_text_sheet.get_value('')):
            rs.open_registration()

    @pytest.mark.parametrize('email, expected', AccountData.email_data)
    @allure.title(report_text_sheet.get_value('') + ': {email}')
    @allure.description(report_text_sheet.get_value(''))
    def test_email_validation(self, driver, email, expected):
        rs = RegistrationSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            rs.fill_email(email)
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(rs.submit_email()).contains(expected)

    @pytest.mark.parametrize('password, confirm, expected', AccountData.password_confirm_data)
    @allure.title(report_text_sheet.get_value('') + ': {password} == {confirm}')
    @allure.description(report_text_sheet.get_value(''))
    def test_password_validation(self, driver, password, confirm, expected):
        rs = RegistrationSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            rs.fill_new_password(password)
        with allure.step(report_text_sheet.get_value('')):
            rs.confirm_password(confirm)
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(rs.submit_password()).contains(expected)
