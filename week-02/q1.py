import numpy as np
# 讀入資料，檔案以","分隔，跳過第一行標題
nf1 = np.genfromtxt('pig.csv',delimiter=',',skip_header=1)
print("市場全年成交最低平均重量"+str(nf1[:,1].min(axis=0)))
print("市場全年成交最高平均價"+str(nf1[:,2].max(axis=0)))
