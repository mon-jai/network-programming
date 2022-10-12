import requests as rq
from bs4 import BeautifulSoup
url = "https://tw.stock.yahoo.com/quote/2330/dividend"  # 網址
html = rq.get(url)  # 讀取靜態網頁html
html.raise_for_status()  # 若沒讀到網頁，回傳error
# print(html.text) # 輸出讀取到的 html
soup = BeautifulSoup(html.text, "html.parser")  # 內建parser分析轉成BeautifulSoup物件
years = soup.find_all("div", class_="D(f) W(98px) Ta(start)")
contexts = soup.find_all(
    "div", class_="Fxg(1) Fxs(1) Fxb(0%) Ta(end) Mend($m-table-cell-space) Mend(0):lc Miw(68px)")

year_input = input()
year_input_2 = input()
sum_of_income = 0
in_range = False

for index, year in enumerate(years):
    if year.text == year_input:
        in_range = True
    if in_range:
        print(f'{year.text}現金股利: {contexts[4 * index].text}')
        sum_of_income += float(contexts[4 * index].text)
        if year.text == year_input_2:
            in_range = False

print(f'加總: {sum_of_income}')
