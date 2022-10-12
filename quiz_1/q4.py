from urllib.request import urlretrieve
import numpy as np

csvFileName, _ = urlretrieve(
    'https://www.bot.com.tw/Govinfo/opendata/csv/233/110GoldPassbook.csv')
# 讀入資料，檔案以","分隔，跳過第一行標題

nf1 = np.genfromtxt(csvFileName, delimiter=',',
                    skip_header=1, encoding='utf-8-sig')

print('日期 本行買入價格 本行賣出價格')
for row in nf1[nf1[:, 3].argsort()][:5]:
    print(f'{row[0]:.0f} {row[3]:.0f} {row[4]:.0f}')
print()

print(f'本行買入價格的中位數：{np.median(nf1[:, 3])}')
print(f'本行賣出價格的平均值：{np.average(nf1[:, 4]):.02f}')
print(f'本行賣出價格的標準差：{np.std(nf1[:, 4]):.02f}')
