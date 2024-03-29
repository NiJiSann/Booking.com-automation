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
    @allure.title(report_text_sheet.get_value('upload_image_preconditions_title'))
    @allure.description(report_text_sheet.get_value('upload_image_preconditions_desc'))
    def test_precondition(self, driver_undetected, email, password):
        rs = SignInSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('open_home')):
            rs.open_page(Urls.HOME_URL)
            rs.close_dialog_modal()
        with allure.step(report_text_sheet.get_value('open_sign_in')):
            rs.open_sign_in()
        with allure.step(report_text_sheet.get_value('fill_email')):
            rs.fill_email(email)
        with allure.step(report_text_sheet.get_value('check_email')):
            rs.submit_email()
        with allure.step(report_text_sheet.get_value('fill_password')):
            rs.fill_password(password)
        with allure.step(report_text_sheet.get_value('sign_in_check_password')):
            rs.submit_password()
        us = UploadProfileImageSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('open_set_image_page')):
            us.open_set_image_page()
        with allure.step(report_text_sheet.get_value('open_image_upload_modal')):
            us.open_modal()

    @allure.title(report_text_sheet.get_value('upload_non_image_title'))
    @allure.description(report_text_sheet.get_value('upload_non_image_desc'))
    def test_upload_non_image(self, driver_undetected):
        us = UploadProfileImageSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('upload_image')):
            us.upload_non_image()
        with allure.step(report_text_sheet.get_value('save_image')):
            us.save_image()
        with soft_assertions(), allure.step(report_text_sheet.get_value('get_image_status')):
            assert_that(us.get_status_note()).contains('Something went wrong')

    @pytest.mark.parametrize('width, height, expected', ImageData.image_size_list)
    @allure.title(report_text_sheet.get_value('upload_image_title') + ': {width} x {height}')
    @allure.description(report_text_sheet.get_value('upload_image_desc'))
    def test_upload_image(self, driver_undetected, width, height, expected):
        us = UploadProfileImageSteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('upload_image')):
            us.upload_image(width, height)
        with allure.step(report_text_sheet.get_value('save_image')):
            us.save_image()
        with soft_assertions(), allure.step(report_text_sheet.get_value('get_image_status')):
            assert_that(us.get_status_note()).contains(expected)
