from typing import List
from urllib.request import urlretrieve
from zipfile import ZipFile
import csv


def print_row(row: List[str]) -> None:
    print(f'{row[0]:>5}{row[1]:>12}{row[2]:>5}{row[3]:>5}{row[8]:>12}{row[12]:>5}')


zipFileName, _ = urlretrieve(
    'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip')

with ZipFile(zipFileName) as zipFile:
    for fileName in zipFile.namelist():
        csvFileName = zipFile.extract(fileName, './')

        with open(csvFileName, 'r', encoding='UTF-8') as csvFile:
            plots = csv.reader(csvFile)

            print_row(plots.__next__())

            for row in plots:
                if int(row[12]) > 5:
                    print_row(row)
