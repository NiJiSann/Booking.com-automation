import gspread


class Table:
    records: dict = None

    @staticmethod
    def load(sheet_title: str = 'Sheet1'):
        gc = gspread.service_account(filename='crids.json')
        sheet = gc.open('Allure Report TextTable').worksheet(sheet_title)
        Table.records = {k: v for (k, v) in sheet.get_all_values()}

    @staticmethod
    def get_value(key: str) -> str:
        return Table.records[key]
