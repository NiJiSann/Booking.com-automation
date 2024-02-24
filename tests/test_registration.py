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
    def test_precondition(self, driver_undetected):
        rs = RegistrationSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('open_home')):
            rs.open_page(Urls.HOME_URL)
            rs.close_dialog_modal()
        with allure.step(report_text_sheet.get_value('open_registration')):
            rs.open_registration()

    @pytest.mark.parametrize('email, expected', AccountData.email_data)
    @allure.title(report_text_sheet.get_value('email_validation_title') + ': {email}')
    @allure.description(report_text_sheet.get_value('email_validation_desc'))
    def test_email_validation(self, driver_undetected, email, expected):
        rs = RegistrationSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('fill_email')):
            rs.fill_email(email)
        with soft_assertions(), allure.step(report_text_sheet.get_value('check_email')):
            assert_that(rs.submit_email()).contains_ignoring_case(expected)

    @pytest.mark.parametrize('password, confirm, expected', AccountData.password_confirm_data)
    @allure.title(report_text_sheet.get_value('password_validation_title') + ': {password} == {confirm}')
    @allure.description(report_text_sheet.get_value('password_validation_desc'))
    def test_password_validation(self, driver_undetected, password, confirm, expected):
        rs = RegistrationSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('fill_new_password')):
            rs.fill_new_password(password)
        with allure.step(report_text_sheet.get_value('confirm_password')):
            rs.confirm_password(confirm)
        with soft_assertions(), allure.step(report_text_sheet.get_value('check_password')):
            assert_that(rs.submit_password()).contains_ignoring_case(expected)
