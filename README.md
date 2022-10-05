# week01

## 04

針對新北市公共自行車即時資訊
顯示空位數量超過 5 的場站資料
包含
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
顯示場站目前有的數量超過 6 的場站資料，
以目前數量大小排序(大->小)顯示
包含
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

將上面XML菜單存檔 menu.xml\
讀取 menu.xml

增加宵夜(Night snack) hours: 21-23\
beer: $10\
skewers: $20\
barbecue: $15

轉成 json 格式存檔成 menu.json

# 09

```
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
2. 讀出 cont2.xml 將所有相鄰國家列出
愛爾蘭:英國
英國:愛爾蘭
...
