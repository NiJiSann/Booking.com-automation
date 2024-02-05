from datetime import date
import re


def get_current_date():
    # the function returns the current date in the format: YYYY-MM-DD.
    return date.today().strftime('%Y-%m-%d')

def get_number(input: str):
    # the function returns the number found in the input string
    number = None
    
    match = re.search(r"\d+,?\d+", input)
    if match:
        number = int(match.group(0).replace(",", ""))
    
    return number