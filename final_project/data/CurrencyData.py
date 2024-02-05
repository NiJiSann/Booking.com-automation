from dataclasses import dataclass


@dataclass
class CurrencyData:
    currency_list = [
        ('USD', 'USD $ US$ $,', 'Currencies are matching'),
        ('JPY', 'JPY ¥, ', 'Currencies are matching'),
        ('EUR', 'EUR € € ', 'Currencies are matching')
    ]