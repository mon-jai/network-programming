# Week 01

## 04

針對新北市公共自行車即時資訊

顯示空位數量超過 5 的場站資料

包含\
sno：站點代號、sna：場站名稱、tot：場站總停車格、sbi：場站目前車輛數量、ar：地址(中文)、bemp：空位數量

## 06

針對全國環境輻射偵測即時資訊

輸入\
一個經緯度(整數)\
經度與緯度偏離值

輸出\
這個經緯度周圍偏離值的監測點和監測值\
以監測值大小排序

例如\
經緯度(整數): 121 25\
經度偏離值 2\
緯度偏離值 2

輸出\
(121-2, 121+2) ~ (25-2, 25+2) 包含區域的監測站的資料

## 07

針對新北市公共自行車即時資訊

讀取 json格式檔案

顯示場站目前有的數量超過 6 的場站資料，\
以目前數量大小排序(大->小)顯示

包含\
sno：站點代號、sna：場站名稱、tot：場站總停車格、sbi：場站目前車輛數量、ar：地址(中文)、bemp：空位數量

## 08

```xml
<?xml version="1.0"?>
<menu>
<breakfast hours="7-11">
<item price="$60">breakfast burritos</item>
<item price="$40">pancakes</item>
</breakfast>
<lunch hours="11-15">
<item price="$50">hamburger</item>
</lunch>
<dinner hours="15-21">
<item price="80">spaghetti</item>
</dinner>
</menu>
```

將上面XML菜單存檔 menu.xml

讀取 menu.xml

增加宵夜(Night snack) hours: 21-23\
beer: $10\
skewers: $20\
barbecue: $15

轉成 json 格式存檔成 menu.json

## 09

```xml
<?xml version="1.0"?>
<data>
<country name="愛爾蘭">
<rank>4</rank>
<year>2017</year>
<gdppc>70638</gdppc>
<neighbor name="英國" direction="北"/>
</country>
<country name="新加坡">
<rank>8</rank>
<year>2017</year>
<gdppc>57713</gdppc>
<neighbor name="馬來西亞" direction="北"/>
</country>
<country name="巴拿馬">
<rank>68</rank>
<year>2011</year>
<gdppc>13600</gdppc>
<neighbor name="哥斯大黎加" direction="西"/>
<neighbor name="哥倫比亞" direction="東"/>
</country>
</data>
```

將上面資料存成 cont.xml 檔案

寫程式讀取 cont.xml

1. 加入新加坡 南邊鄰國 亞特蘭提斯，修改愛爾蘭 gdppc 值 88888，寫入 cont2.xml
2. 讀出 cont2.xml 將所有相鄰國家列出\
愛爾蘭:英國\
英國:愛爾蘭\
...

# Week 02

## 01

載入 pig.csv

輸出全年成交最低平均重量的成交頭數 e.g. 2146\
輸出全年成交最高平均價格的成交頭數 e.g. 1456

## 02

載入 pig.csv

輸出全年成交平均重量的標準差 e.g. 2.3954\
輸出全年成交平均價格的中位數 e.g. 70.82\
輸出全年成交平均重量的第三個四分位數 124.1

## 03

載入 pig.csv

輸出全年成交平均重量的成交頭數，最低前 5 筆資料(平均重量)\
eg.\
101\
100\
90\
101\
90

輸出全年成交平均價格的成交頭數，最高前 5 筆資料(平均價格)\
eg.\
90\
90\
91\
91\
100

輸出全年成交平均重量的成交頭數，最低前 5 筆資料，原本資料的次序編號\
eg.\
295\
546\
1255\
2973\
2084

## 04

使用 Pandas

載入 president_heights.csv

輸出總統身高的敘述統計資料\
輸出總統身高，最高前 5 筆資料\
輸出總統身高 > 180，最低的 5 筆資料

## 05

使用 Pandas

載入 bike.json

1. 找出空位數大於 10 的站點資料，輸出所在區、站點名稱、地址、空位數\
eg. 新店區 大鵬華城 新北市新店區中正路700巷3號 14

2. 根據第一點的資料，\
統計出每一區(新店區、板橋區、....)空位數大於 10 的資料，\
輸出每一區空位數大於 10 的所有站點個數\
eg. 新店區 15

3. 根據第一點的資料，\
統計出每一區(新店區、板橋區、....)空位數大於 10 的資料，\
輸出每一區空位數大於 10 的所有加總空位數\
e.g.\
新店區 30\
板橋區 50

## 06

https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx

使用 pandas

計算 2002 年全球人口各國平均數\
計算 2002 年全球各洲平均壽命、平均財富

# Week 03

## 01

隨機亂數產生全班N ( 輸入)位學成績，0~100\
畫四個子圖，每一個子圖要有標題、刻度、標籤樣式

1. 長條圖 統計及格與不及格人數
2. 折線圖 x 分數， y 人數，每五分一個區間
3. 散射圖 x 分數， y 人數，每 10 分一個區間，自訂一個 mark
4. 圓餅圖 81~100, 60~80, 0~59 三塊餅

## 02

查詢台銀牌告匯率

找出現金買入和賣出利差最多的前三名

## 03

查詢三個城市

找出小七店最多個數的街/路前三名

# Week 04

## 04

環保署AQI 公開資料集

輸入城市名稱、PM2.5 值以上
輸出查詢資料 County, SiteName, AQI, PM2.5 avg, Status

臺北市
8

SQL 變成字串
欄位名稱，用雙引號括起來
```SQL
SELECT 欄位名稱1,欄位名稱2 #顯示欄位資料
FROM table_name #哪一個資料庫表格
WHERE condition1 AND condition2 #過濾條件
ORDER BY 欄位名稱 #排序欄位
```

## 05

新北市不動產仲介經紀商業同業公會會員資料查詢
1. 公司名稱關鍵字
2. 公司地址關鍵字

input
1
產業

output
列出所有公司名稱有"產業"

input
2
中山路

output
列出所有公司地址有"中山路"


# Cleaning up

```powershell
Remove-Item "$Env:LOCALAPPDATA\Google\Chrome\User Data\" -Force -Recurse -ErrorAction SilentlyContinue
```
