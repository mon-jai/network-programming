from functools import cmp_to_key
from typing import NamedTuple

import requests
from bs4 import BeautifulSoup, Tag


class EarthQuake (NamedTuple):
    time: str
    depth: float
    intensity: float
    location: str

    def __str__(self):
        return f'{self.time} {self.depth:g} {self.intensity} {self.location}'


def compare(a: EarthQuake, b: EarthQuake):
    if a.intensity > b.intensity:
        return 1
    elif a.intensity == b.intensity and a.depth < b.depth:
        return 1
    else:
        return -1


html = requests.get('https://scweb.cwb.gov.tw/zh-tw/earthquake/world/#').text
bsObj = BeautifulSoup(html, "lxml")

table = bsObj.find("table", class_="Btable worldTable")
assert isinstance(table, Tag)

earthQuakes = [
    EarthQuake(
        tds[0].text, float(tds[3].text),
        float(tds[4].text), tds[5].text.strip()
    )
    for tds in (
        tr.findAll('td')
        for tr in table.findAll('tr')[1:]
    )
]
earthQuakes.sort(key=cmp_to_key(compare), reverse=True)

print('地震時間 深度 規模 地震位置')
print('\n'.join([str(earthQuake) for earthQuake in earthQuakes][:3]))
