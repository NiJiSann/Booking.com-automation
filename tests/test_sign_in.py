import allure
from API.GSpread.allure_report_texts import Table as report_text_sheet
import pytest
from final_project.data.AccountData import AccountData
from final_project.data.CommonData import Urls
from final_project.steps.SignInSteps import SignInSteps
from assertpy import assert_that, soft_assertions


@allure.feature(report_text_sheet.get_value('additional'))
class TestSignIn:
    @allure.title(report_text_sheet.get_value('sign_in_preconditions_title'))
    @allure.description(report_text_sheet.get_value('sign_in_preconditions_desc'))
    def test_precondition(self, driver_undetected):
        rs = SignInSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('open_home')):
            rs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('refresh')):
            rs.driver.refresh()
        with allure.step(report_text_sheet.get_value('open_sign_in')):
            rs.open_sign_in()

    @pytest.mark.parametrize('email, expected', AccountData.sign_in_email_data)
    @allure.title(report_text_sheet.get_value('email_validation_title') + ': {email}')
    @allure.description(report_text_sheet.get_value('email_validation_desc'))
    def test_email_validation(self, driver_undetected, email, expected):
        rs = SignInSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('fill_email')):
            rs.fill_email(email)
        with soft_assertions(), allure.step(report_text_sheet.get_value('check_email')):
            assert_that(rs.submit_email()).contains(expected)

    @pytest.mark.parametrize('password, expected', AccountData.sign_in_password_data)
    @allure.title(report_text_sheet.get_value('sign_in_password_validation_title') + ': {password}')
    @allure.description(report_text_sheet.get_value('sign_in_password_validation_desc'))
    def test_password_validation(self, driver_undetected, password, expected):
        rs = SignInSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('fill_password')):
            rs.fill_password(password)
        with soft_assertions(), allure.step(report_text_sheet.get_value('sign_in_check_password')):
            assert_that(rs.submit_password()).contains(expected)
