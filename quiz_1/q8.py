import re

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def sort_results(row: tuple[str, str, str]) -> str:
    match = re.search(r'^.*[市縣]', row[2])
    return f'{match.group(0) if match else row[2]} {row[0]}'


def printRow(row: tuple[str, str, str]):
    print(' '.join(column for column in row))


strKeyWords = input()

html = requests.post(
    'https://www.ibon.com.tw/retail_inquiry_ajax.aspx',
    data={"strTargetField": "MIXFIELD", "strKeyWords": strKeyWords}
).text

bsObj = BeautifulSoup(html, "lxml")
table = bsObj.find("table")
assert isinstance(table, Tag)

data: list[tuple[str, str, str]] = [
    (tds[0].text, tds[1].text, tds[2].text)
    for tds in (
        tr.findAll("td")
        for tr in table.findAll("tr")
    )
]

printRow(data[0])

data.pop(0)
data.sort(key=sort_results)

for row in data:
    printRow(row)
