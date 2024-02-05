from final_project.pages.CommopPage import CommonPage as cp
from final_project.pages.ChangeCurrencyPage import ChangeCurrencyPage as ccp
from final_project.steps.common_actions import Common


class ChangeCurrencySteps(Common):
    def choose_currency(self, currency):
        self.click(cp.CURRENCY_PICKER)
        self.click(ccp.get_currency_locator(currency))

    def compare_stays_price_currency(self):
        pass

    def compare_attraction_price_currency(self):
        pass

    def compare_car_rental_price_currency(self):
        pass

    def compare_taxi_price_currency(self):
        pass

    def compare_flight_price_currency(self):
        pass



