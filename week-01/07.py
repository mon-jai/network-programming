from typing import Any, List, Dict
from urllib.request import urlretrieve
import json


def print_row(row: List[str]) -> None:
    print(' '.join(row))


jsonFileName, _ = urlretrieve(
    'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json')

with open(jsonFileName, 'r', encoding='UTF-8') as jsonFile:
    data: List[Dict[str, Any]] = json.load(jsonFile)

    print_row(list(data[0].keys()))

    for row in data:
        if int(row['sbi']) > 5:
            print_row(list(row.values()))
