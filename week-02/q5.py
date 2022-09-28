from pandas import read_json

data = read_json("bike.json")

# sno：站點代號、sna：場站名稱、tot：場站總停車格、sbi：場站目前車輛數量、ar：地址(中文)、bemp：空位數量
print(data[data['bemp'].astype(int) > 10][['sarea', 'sna', 'ar', 'bemp']])
print(data[data['bemp'].astype(int) > 10].groupby('sarea')['sno'].count())
print(data[data['bemp'].astype(int) > 10].groupby('sarea')['bemp'].sum())
