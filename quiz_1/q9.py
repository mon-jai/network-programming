import enum
from typing import NamedTuple

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class Winning_Numbers(NamedTuple):
    special_prize_number: str
    first_prize_number: str
    grand_prize_numbers: str


def get_prize_number(announcement_url: str):
    response = requests.get(announcement_url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")

    special_prize_number = ""
    first_prize_number = ""
    grand_prize_numbers = []

    table = soup.find(id="tenMillionsTable")
    assert isinstance(table, Tag)

    for tr in table.find_all("tr"):
        th = tr.find("th")

        if th == None:
            continue

        heading = th.text

        if heading == "特別獎":
            special_prize_number = tr.find(class_="row").text.strip()
        elif heading == "特獎":
            first_prize_number = tr.find(class_="row").text.strip()
        elif heading == "頭獎":
            grand_prize_numbers = tr.find(class_="row").text.split()

    return Winning_Numbers(
        special_prize_number, first_prize_number, grand_prize_numbers
    )


prize_amounts = {
    "特別獎": 10000000,
    "特獎": 2000000,
    "頭獎": 200000,
    "二獎": 40000,
    "三獎": 10000,
    "四獎": 4000,
    "五獎": 1000,
    "六獎": 200,
    "無": 0,
}

no_of_invoice = int(input())
invoice_numbers = [input() for _ in range(no_of_invoice)]
month = int(input())
total_price = 0

announcement_url = (
    'https://www.etax.nat.gov.tw/etw-main/ETW183W2_11101/'
    if month in (1, 2)
    else 'https://www.etax.nat.gov.tw/etw-main/ETW183W2_11103/'
    if month in (3, 4)
    else 'https://www.etax.nat.gov.tw/etw-main/ETW183W2_11105/'
    if month in (5, 6)
    else 'https://www.etax.nat.gov.tw/etw-main/ETW183W2_11107/'
)

special_prize_number, first_prize_number, grand_prize_numbers = get_prize_number(
    announcement_url
)

for invoice_number in invoice_numbers:
    prize = '無'

    if invoice_number == special_prize_number:
        prize = '特別獎'
    elif invoice_number == first_prize_number:
        prize = '特獎'
    elif invoice_number in grand_prize_numbers:
        prize = '頭獎'
    else:
        no_of_matching_digits = []


        for grand_prize_number in grand_prize_numbers:
            no_of_matching_digit = 0

            for index, character in enumerate(grand_prize_number[::-1]):
                if character == invoice_number[7 - index]:
                    no_of_matching_digit += 1
                else:
                    break

            no_of_matching_digits.append(no_of_matching_digit)

        no_of_matching_digit = max(no_of_matching_digits)

        if no_of_matching_digit == 7:
            prize = '二獎'
        elif no_of_matching_digit == 6:
            prize = '三獎'
        elif no_of_matching_digit == 5:
            prize = '四獎'
        elif no_of_matching_digit == 4:
            prize = '五獎'
        elif no_of_matching_digit == 3:
            prize = '六獎'

    total_price += prize_amounts[prize]
    print(f'{invoice_number} {prize} {prize_amounts[prize]}')

print(f'total_price：{total_price}')
