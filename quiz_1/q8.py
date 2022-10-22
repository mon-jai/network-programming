from functools import cmp_to_key
import re

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def extract_city(address: str) -> str:
    result = re.search(r'(?P<city>^.*[市縣])', address)
    assert result is not None
    return result.group('city')


def extract_house_number(address: str):
    result = re.search(r'(?P<house_number>\d+)號', address)
    assert result is not None
    return int(result.group('house_number'))


def compare(a: tuple[str, str, str], b: tuple[str, str, str]):
    city_a = extract_city(a[2])
    city_b = extract_city(b[2])
    house_number_a = extract_house_number(a[2])
    house_number_b = extract_house_number(b[2])

    if city_a > city_b:
        return 1
    elif city_a < city_b:
        return -1
    else:
        return (
            0
            if house_number_a == house_number_b
            else 1
            if house_number_a > house_number_b
            else -1
        )


def printRow(row: tuple[str, str, str]):
    print(' '.join(column for column in row))


strKeyWords = input()

html = requests.post(
    'https://www.ibon.com.tw/retail_inquiry_ajax.aspx',
    data={"strTargetField": "MIXFIELD", "strKeyWords": strKeyWords},
).text

bsObj = BeautifulSoup(html, "lxml")
table = bsObj.find("table")
assert isinstance(table, Tag)

data: list[tuple[str, str, str]] = [
    (tds[0].text, tds[1].text, tds[2].text)
    for tds in (tr.findAll("td") for tr in table.findAll("tr"))
]

printRow(data[0])

data.pop(0)
data.sort(key=cmp_to_key(compare))

for row in data:
    printRow(row)

# 承德路
