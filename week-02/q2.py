import numpy as np
# 讀入資料，檔案以","分隔，跳過第一行標題
nf1 = np.genfromtxt('pig.csv', delimiter=',', skip_header=1)
print("全年成交平均重量的標準差"+str(np.std(nf1[:, 1])))
print("全年成交平均價格的中位數"+str(np.median(nf1[:, 2])))
print("全年成交平均重量的第三個四分位數"+str(np.percentile(nf1[:, 1], 75)))
