from typing import Any, List, Dict
from urllib.request import urlretrieve
import json

jsonFileName, _ = urlretrieve(
    'https://data.ntpc.gov.tw/api/datasets/1688B7B8-106E-4967-AA38-DBD86D81D495/json/preview')

print('sta add no')

with open(jsonFileName, 'r', encoding='UTF-8') as jsonFile:
    data: List[Dict[str, Any]] = json.load(jsonFile)

    for station in data:
        if station['cha'] == '是' and station['ope'] == '否':
            print(f'{station["sta"]} {station["add"]} {station["no"]}')
