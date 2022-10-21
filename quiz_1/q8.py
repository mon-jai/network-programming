from functools import cmp_to_key
import re

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

def compare(a, b):
    city_1 = re.search(r'^.*[市縣]', a[2]).group(0)
    city_2 = re.search(r'^.*[市縣]', b[2]).group(0)
    door_1 = int(re.search(r'(\d+)號', a[2]).group(1))
    door_2 = int(re.search(r'(\d+)號', b[2]).group(1))

    if city_1 > city_2:
        return 1 
    elif city_1 < city_2:
        return -1
    else:
        return 1 if door_1 > door_2 else -1

def printRow(row):
    print(' '.join(column for column in row))


strKeyWords = input()

html = requests.post(
    'https://www.ibon.com.tw/retail_inquiry_ajax.aspx',
    data={"strTargetField": "MIXFIELD", "strKeyWords": strKeyWords}
).text

bsObj = BeautifulSoup(html, "lxml")
table = bsObj.find("table")
assert isinstance(table, Tag)

data = [
    (tds[0].text, tds[1].text, tds[2].text)
    for tds in (
        tr.findAll("td")
        for tr in table.findAll("tr")
    )
]

printRow(data[0])

data.pop(0)
data.sort(key=cmp_to_key(compare))

for row in data:
    printRow(row)


# 承德路
