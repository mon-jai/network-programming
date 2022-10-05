# 抓取7-eleven各門市資訊
import requests  # 抓取網頁的套件
import pandas as pd  # 分析資料的套件
# 建立一個縣市的list
city = ['基隆市', '台北市', '新北市', '桃園市']
# 使用迴圈依序取得每一個城市的門市資訊
roadAddressRecord = {}
for index, city in enumerate(city):
    # 剛在網頁開發者模式觀察到的Post發出的資訊
    data = {'strTargetField': 'COUNTY', 'strKeyWords': '%s' % city}
    # res 取得網頁所有資料
    res = requests.post(
        'https://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)
    # 本次城市門市個數
    count = pd.read_html(res.text, header=0)[0].shape[0]
    # 取得本次城市門市資料
    data = pd.read_html(res.text, header=0)[0]

    for i in range(count):
        # 第三欄資料為地址 iloc[i,2]
        fullAddress = data.iloc[i, 2]
        # 找城市名稱開頭,路結尾的地址字串
        start = fullAddress.find(city[0])
        end = fullAddress.find('路')+1
        #end = fullAddress.find('街')+1
        if end < 3:
            continue  # 空的資料跳過
        roadAddress = fullAddress[start:end]
        # print(roadAddress)
        if roadAddress not in roadAddressRecord:
            roadAddressRecord[roadAddress] = 1
        else:
            roadAddressRecord[roadAddress] += 1

print('\n'.join(
    f'{key}, {value}'
    for key, value in sorted(roadAddressRecord.items(), key=lambda item: item[1], reverse=True)[:3]
))
