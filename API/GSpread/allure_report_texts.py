import gspread


class Table:
    def __init__(self, sheet_title: str = 'Sheet1'):
        self.gc = gspread.service_account(filename='crids.json')
        self.sheet = self.gc.open('Allure Report TextTable').worksheet(sheet_title)
        self.records: dict = {k: v for (k, v) in self.sheet.get_all_values()}

    def get_value(self, key: str) -> str:
        return self.records[key]
