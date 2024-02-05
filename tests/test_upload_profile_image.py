import time

import pytest
from final_project.steps.SignInSteps import SignInSteps
from final_project.data.CommonData import Urls
from final_project.steps.UploadProfileImageSteps import UploadProfileImageSteps
from final_project.data.ImageData import ImageData
from assertpy import assert_that, soft_assertions


class TestUploadProfileImage:

    @pytest.mark.parametrize('email, password',
                             [('sabrorxojaev2@gmail.com', 'CorrectPassword1')])
    def test_precondition(self, driver_undetected, email, password):
        rs = SignInSteps(driver_undetected)
        rs.open_page(Urls.HOME_URL)
        rs.driver.refresh()
        time.sleep(1)
        rs.open_sign_in()
        rs.fill_email(email)
        rs.submit_email()
        rs.fill_password(password)
        rs.submit_password()
        us = UploadProfileImageSteps(driver_undetected)
        us.open_set_image_page()
        us.open_modal()

    def test_upload_non_image(self, driver_undetected):
        us = UploadProfileImageSteps(driver_undetected)
        us.upload_non_image(ImageData.non_image_type_file)
        us.save_image()
        with soft_assertions():
            assert_that(us.get_status_note()).contains('Something went wrong')

    @pytest.mark.parametrize('width, height, expected', ImageData.image_size_list)
    def test_upload_image(self, driver_undetected, width, height, expected):
        us = UploadProfileImageSteps(driver_undetected)
        us.upload_image(width, height)
        us.save_image()
        with soft_assertions():
            assert_that(us.get_status_note()).contains(expected)
