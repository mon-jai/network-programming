import requests  # 匯入套件
from bs4 import BeautifulSoup  # 解析網頁

# 回傳HTML檔案，轉存html物件
html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html.content, "lxml")  # 解析網頁，建立bs物件

results = []

# 針對匯率表格分析
for single_tr in bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr"):
    cell = single_tr.findAll("td")  # 找到每一個表格
    currency_name = cell[0].find(
        "div", {"class": "visible-phone"}).contents[0]  # 找到表格中幣別
    currency_name = currency_name.replace("\r", "")  # 取代不需要的字元
    currency_name = currency_name.replace("\n", "")
    currency_name = currency_name.replace(" ", "")
    try:
        currency_rate_difference = abs(
            float(cell[1].contents[0]) - float(cell[2].contents[0]))  # 找到幣別匯率
        results.append((currency_name, currency_rate_difference))
    except:
        pass

results.sort(key=lambda result: result[0], reverse=True)

print('\n'.join(name for name, _ in results[:3]))
