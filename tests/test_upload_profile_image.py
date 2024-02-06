import time
import allure
import pytest
from final_project.steps.SignInSteps import SignInSteps
from final_project.data.CommonData import Urls
from final_project.steps.UploadProfileImageSteps import UploadProfileImageSteps
from final_project.data.ImageData import ImageData
from assertpy import assert_that, soft_assertions
from API.GSpread.allure_report_texts import Table as report_text_sheet


@allure.feature(report_text_sheet.get_value('additional'))
class TestUploadProfileImage:

    @pytest.mark.parametrize('email, password',
                             [('sabrorxojaev2@gmail.com', 'CorrectPassword1')])
    @allure.title(report_text_sheet.get_value(''))
    @allure.description(report_text_sheet.get_value(''))
    def test_precondition(self, driver_undetected, email, password):
        rs = SignInSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            rs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            rs.driver.refresh()
        time.sleep(1)
        with allure.step(report_text_sheet.get_value('')):
            rs.open_sign_in()
        with allure.step(report_text_sheet.get_value('')):
            rs.fill_email(email)
        with allure.step(report_text_sheet.get_value('')):
            rs.submit_email()
        with allure.step(report_text_sheet.get_value('')):
            rs.fill_password(password)
        with allure.step(report_text_sheet.get_value('')):
            rs.submit_password()
        us = UploadProfileImageSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            us.open_set_image_page()
        with allure.step(report_text_sheet.get_value('')):
            us.open_modal()

    @allure.title(report_text_sheet.get_value(''))
    @allure.description(report_text_sheet.get_value(''))
    def test_upload_non_image(self, driver_undetected):
        us = UploadProfileImageSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            us.upload_non_image(ImageData.non_image_type_file)
        with allure.step(report_text_sheet.get_value('')):
            us.save_image()
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(us.get_status_note()).contains('Something went wrong')

    @pytest.mark.parametrize('width, height, expected', ImageData.image_size_list)
    @allure.title(report_text_sheet.get_value('') + ': {width} x {height}')
    @allure.description(report_text_sheet.get_value(''))
    def test_upload_image(self, driver_undetected, width, height, expected):
        us = UploadProfileImageSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            us.upload_image(width, height)
        with allure.step(report_text_sheet.get_value('')):
            us.save_image()
        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(us.get_status_note()).contains(expected)
