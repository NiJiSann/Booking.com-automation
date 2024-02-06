import allure
import pytest
from final_project.data.CommonData import Urls
from assertpy import assert_that, soft_assertions
from final_project.steps.ChangeCurrencySteps import ChangeCurrencySteps
from final_project.data.CurrencyData import CurrencyData
from API.GSpread.allure_report_texts import Table as report_text_sheet


@allure.feature(report_text_sheet.get_value('additional'))
class TestChangingCurrency:

    @allure.title(report_text_sheet.get_value(''))
    @allure.description(report_text_sheet.get_value(''))
    def test_precondition(self, driver_undetected):
        ccs = ChangeCurrencySteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            ccs.open_page(Urls.HOME_URL)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    @allure.title(report_text_sheet.get_value('') + ': {website_currency}')
    @allure.description(report_text_sheet.get_value(''))
    def test_stays_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            ccs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            try:
                ccs.choose_currency(website_currency)
            except:
                ccs.driver.refresh()
                ccs.choose_currency(website_currency)

        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(ccs.get_stays_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    @allure.title(report_text_sheet.get_value('') + ': {website_currency}')
    @allure.description(report_text_sheet.get_value(''))
    def test_attraction_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            ccs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            try:
                ccs.choose_currency(website_currency)
            except:
                ccs.driver.refresh()
                ccs.choose_currency(website_currency)

        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(ccs.get_attraction_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    @allure.title(report_text_sheet.get_value('') + ': {website_currency}')
    @allure.description(report_text_sheet.get_value(''))
    def test_car_rental_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            ccs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            try:
                ccs.choose_currency(website_currency)
            except:
                ccs.driver.refresh()
                ccs.choose_currency(website_currency)

        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(ccs.get_car_rental_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    @allure.title(report_text_sheet.get_value('') + ': {website_currency}')
    @allure.description(report_text_sheet.get_value(''))
    def test_taxi_currency_change(self, driver_undetected, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver_undetected)
        with allure.step(report_text_sheet.get_value('')):
            ccs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            try:
                ccs.choose_currency(website_currency)
            except:
                ccs.driver.refresh()
                ccs.choose_currency(website_currency)

        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(ccs.get_taxi_price_currency(match_currency)).is_equal_to(expected)

    @pytest.mark.parametrize('website_currency, match_currency, expected', CurrencyData.currency_list)
    @allure.title(report_text_sheet.get_value('') + ': {website_currency}')
    @allure.description(report_text_sheet.get_value(''))
    def test_flights_currency_change(self, driver, website_currency, match_currency, expected):
        ccs = ChangeCurrencySteps(driver)
        with allure.step(report_text_sheet.get_value('')):
            ccs.open_page(Urls.HOME_URL)
        with allure.step(report_text_sheet.get_value('')):
            try:
                ccs.choose_currency(website_currency)
            except:
                ccs.driver.refresh()
                ccs.choose_currency(website_currency)

        with soft_assertions(), allure.step(report_text_sheet.get_value('')):
            assert_that(ccs.get_flight_price_currency(match_currency)).is_equal_to(expected)
