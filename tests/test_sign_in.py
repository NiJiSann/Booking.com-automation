import allure
from API.GSpread.allure_report_texts import Table as report_text_sheet
import pytest
from final_project.data.AccountData import AccountData
from final_project.data.CommonData import Urls
from final_project.steps.SignInSteps import SignInSteps
from assertpy import assert_that, soft_assertions


@allure.feature(report_text_sheet.get_value('additional'))
class TestSignIn:
    @allure.title(report_text_sheet.get_value(''))
    @allure.description(report_text_sheet.get_value(''))
    def test_precondition(self, driver):
        rs = SignInSteps(driver)
        with allure.step(report_text_sheet.get_value('open page')):
            rs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            rs.driver.refresh()
        with allure.step(''):
            rs.open_sign_in()

    @pytest.mark.parametrize('email, expected', AccountData.sign_in_email_data)
    @allure.title(report_text_sheet.get_value('') + ': {email}')
    @allure.description(report_text_sheet.get_value(''))
    def test_email_validation(self, driver, email, expected):
        rs = SignInSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            rs.fill_email(email)
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(rs.submit_email()).contains(expected)

    @pytest.mark.parametrize('password, expected', AccountData.sign_in_password_data)
    @allure.title(report_text_sheet.get_value('') + ': {password}')
    @allure.description(report_text_sheet.get_value(''))
    def test_password_validation(self, driver, password, expected):
        rs = SignInSteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            rs.fill_password(password)
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(rs.submit_password()).contains(expected)
