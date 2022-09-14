from typing import List
from urllib.request import urlretrieve
from zipfile import ZipFile
import csv
from pandas import DataFrame


def print_row(row: List[str]) -> None:
    DataFrame(row[0], row[1], row[2], row[3], row[8], row[12])


zipFileName, _ = urlretrieve(
    'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip')

with ZipFile(zipFileName) as zipFile:
    for fileName in zipFile.namelist():
        csvFileName = zipFile.extract(fileName, './')

        with open(csvFileName, 'r', encoding='UTF-8') as csvFile:
            plots = csv.reader(csvFile)

            header = plots.__next__()

            print(DataFrame([[row[0], row[1], row[2], row[3], row[8], row[12]]
                            for row in plots if int(row[12]) > 5], [header[0], header[1], header[2], header[3], header[8], header[12]]))
