import json
import time
from final_project.data.login_cookies import cookies as login_cookie
from final_project.data.CommonData import Urls
from final_project.steps.UploadProfileImageSteps import UploadProfileImageSteps


class TestUploadProfileImage:

    def test_precondition(self,  driver):
        us = UploadProfileImageSteps(driver)
        us.open_page(Urls.HOME_URL)
        for cookie in login_cookie:
            driver.add_cookie({k: cookie[k] for k in {'name', 'value'}})
        driver.refresh()
        time.sleep(60)

