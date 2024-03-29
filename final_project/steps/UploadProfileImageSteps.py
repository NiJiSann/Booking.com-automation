from final_project.pages.AccountSettingsPage import AccountSettingsPage as asp
from final_project.pages.PersonalDetailsPage import PersonalDetailsPage as pdp
from final_project.pages.CommopPage import CommonPage as cp
from final_project.steps.common_actions import Common
from API.RandomImage.image import Image


class UploadProfileImageSteps(Common):

    def open_set_image_page(self):
        self.click(cp.YOUR_ACCOUNT)
        self.click(cp.MANAGE_ACCOUNT)
        self.click(asp.PERSONAL_DETAILS)

    def open_modal(self):
        self.click(pdp.SET_PROFILE_IMAGE_MODAL)

    def upload_image(self, width, height):
        path = Image.download('img.jpg', width, height)
        self.wait_for(pdp.IMAGE_INPUT).send_keys(path)

    def upload_non_image(self):
        path = Image.download('img.bin', 100, 100)
        self.wait_for(pdp.IMAGE_INPUT).send_keys(path)

    def get_status_note(self) -> str:
        status = self.wait_for(pdp.STATUS_NOTE).text
        return status

    def save_image(self):
        self.click(pdp.SAVE_IMAGE)



