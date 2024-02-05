from final_project.pages.car_rental_search_result_page import CarRentalSearchResultPage
from final_project.steps.my_common_actions import MyCommonActions


class CarRentalSearchResultStep(MyCommonActions, CarRentalSearchResultPage):
    def get_page_title(self):
        self.get_text(self.TITLE)