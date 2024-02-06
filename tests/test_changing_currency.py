import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
from final_project.steps.ChangeCurrencySteps import ChangeCurrencySteps
from final_project.data.CurrencyData import CurrencyData


class TestChangingCurrency:
    def test_precondition(self, driver_undetected):
        ccs = ChangeCurrencySteps(driver_undetected)
        ccs.open_page(Urls.HOME_URL)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    def test_stays_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        ccs.open_page(Urls.HOME_URL)
        try:
            ccs.choose_currency(website_currency)
        except:
            ccs.driver.refresh()
            ccs.choose_currency(website_currency)

        with soft_assertions():
            assert_that(ccs.get_stays_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    def test_attraction_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        ccs.open_page(Urls.HOME_URL)
        try:
            ccs.choose_currency(website_currency)
        except:
            ccs.driver.refresh()
            ccs.choose_currency(website_currency)

        with soft_assertions():
            assert_that(ccs.get_attraction_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    def test_car_rental_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        ccs.open_page(Urls.HOME_URL)
        try:
            ccs.choose_currency(website_currency)
        except:
            ccs.driver.refresh()
            ccs.choose_currency(website_currency)

        with soft_assertions():
            assert_that(ccs.get_car_rental_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    def test_taxi_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        ccs.open_page(Urls.HOME_URL)
        try:
            ccs.choose_currency(website_currency)
        except:
            ccs.driver.refresh()
            ccs.choose_currency(website_currency)

        with soft_assertions():
            assert_that(ccs.get_taxi_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    def test_flights_currency_change(self, driver, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver)
        ccs.open_page(Urls.HOME_URL)
        try:
            ccs.choose_currency(website_currency)
        except:
            ccs.driver.refresh()
            ccs.choose_currency(website_currency)

        with soft_assertions():
            assert_that(ccs.get_flight_price_currency(match_currency)).is_equal_to(expected)
