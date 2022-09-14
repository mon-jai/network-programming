from typing import List
from urllib.request import urlretrieve
import csv

csvFileName, _ = urlretrieve('https://www.aec.gov.tw/dataopen/index.php?id=2')

long, lat = [int(value) for value in input().split()]
residual = int(input())

with open(csvFileName, 'r', encoding='big5') as csvFile:
    plots = csv.reader(csvFile, delimiter=',')

    header = plots.__next__()
    results: List[List[str]] = []

    for row in plots:
        if abs(float(row[4]) - long) < residual and abs(float(row[5]) - lat) < residual:
            results.append(row)

    results.sort(key=lambda row: row[2], reverse=True)

    print(' '.join(header))

    for row in results:
        print(' '.join(row))
