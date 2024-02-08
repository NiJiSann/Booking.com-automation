import os.path

import gspread


class Table:
    records: dict = None

    @staticmethod
    def load():
        gc = gspread.service_account('crids.json')
        sheet = gc.open('Allure Report TextTable').worksheet('Sheet1')
        Table.records = {k: v for (k, v) in sheet.get_all_values()}

    @staticmethod
    def get_value(key: str) -> str:
        return Table.records[key]
