from urllib.request import urlretrieve
from zipfile import ZipFile
import csv


def extract_and_print(row):
    print(f'{row[0]} {row[1]} {row[12]}')


zipFileName, _ = urlretrieve('https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
                             )
with ZipFile(zipFileName) as zipFile:
    for fileName in zipFile.namelist():
        csvFileName = zipFile.extract(fileName, './')

        with open(csvFileName, 'r', encoding='UTF-8') as csvFile:
            plots = csv.reader(csvFile)

            '''
            0 "sno"
            1 sna
            2 tot
            3 sbi
            4 sarea
            5 mday
            6 lat
            7 lng
            8 ar
            9 sareaen
            10 snaen
            11 aren
            12 bemp
            13 act
            print('\n'.join(f'{index} {col}' for index, col in enumerate(plots.__next__())))
            '''

            extract_and_print(plots.__next__())

            data = [row for row in plots]
            data.sort(key=lambda row: int(row[12]), reverse=True)

            for row in sorted(data[0:5], key=lambda row: row[0]):
                extract_and_print(row)
