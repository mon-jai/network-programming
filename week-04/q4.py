import json
import requests
import pandas as pd
from sqlalchemy import create_engine
# 環保署開放資料API網址，用requests的get方法取得檔案，設為req物件
req = requests.get('http://opendata2.epa.gov.tw/AQI.json')
# loads方法解析req物件，存為data物件
data = json.loads(req.content.decode('utf8'))
df = pd.DataFrame(data)  # 解析為pandas的DataFrame結構
# 用sqlalchemy模組create_engine建立sqlite連線，將資料表儲存在memory
engine = create_engine('sqlite:///:memory:')
# 將df利用to_sql方法指定給'AQI_table'
# 用SQL語法顯示縣市、區域、PM2.5，並以PM2.5排序
df.to_sql('AQI_table', engine, index=False)

city_name = input()
pm = int(input())

print(pd.read_sql_query(f'SELECT County, SiteName, AQI,  CAST("PM2.5_AVG" AS int) as "PM2.5_AVG", Status \
FROM "AQI_table" \
where "County" = "{city_name}" and CAST(`PM2.5_AVG` AS int) > {pm}', engine))
