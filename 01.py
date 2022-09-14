from typing import List
from urllib import request
from zipfile import ZipFile
import csv


def print_row(row: List[str]) -> None:
    print(f'{row[0]:>5}{row[1]:>12}{row[3]:>5}{row[12]:>5}')


zipFileName, _ = request.urlretrieve(
    'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip')

with ZipFile(zipFileName) as zipFile:
    for fileName in zipFile.namelist():
        zipFile.extract(fileName, './')
        print(fileName)

        with open(fileName, 'r', encoding='UTF-8') as csvFile:
            plots = csv.reader(csvFile, delimiter=',')

            print_row(plots.__next__())

            for row in plots:
                if int(row[12]) > 5:
                    print_row(row)
