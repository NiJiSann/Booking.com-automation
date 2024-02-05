from final_project.pages.AccountSettingsPage import AccountSettingsPage as asp
from final_project.pages.PersonalDetailsPage import PersonalDetailsPage as pdp
from final_project.pages.CommopPage import CommonPage as cp
from final_project.steps.common_actions import Common
from API.RandomImage.image import Image


class UploadProfileImageSteps(Common):

    error_message = ''

    def open_set_image_modal(self):
        self.click(cp.YOUR_ACCOUNT)
        self.click(cp.MANAGE_ACCOUNT)
        self.click(asp.PERSONAL_DETAILS)
        self.click(pdp.SET_PROFILE_IMAGE_MODAL)

    def upload_image(self, width, height):
        path = Image.download(width, height)
        self.wait_for(pdp.IMAGE_INPUT).send_keys(path)
        self.error_message = self.find(pdp.STATUS_NOTE).text

    def upload_non_image(self, file_path):
        self.wait_for(pdp.IMAGE_INPUT).send_keys(file_path)
        self.error_message = self.find(pdp.STATUS_NOTE).text

    def get_status_note(self) -> str:
        status = self.get_text(pdp.STATUS_NOTE)
        if status.__contains__("Successfully"):
            return status
        return self.error_message

    def save_image(self):
        self.click(pdp.SAVE_IMAGE)



