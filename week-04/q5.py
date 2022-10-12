from urllib.request import urlopen
from bs4 import BeautifulSoup

type = int(input())
table_index = 0 if type == 1 else 4
search_term = input()

httphead = "http://www.tcr.org.tw/a/table_blogs/index/21654"
# 根據新北市不動產仲介經紀商業同業公會網站會員介紹首頁
# 與其後各頁差異，根據頁面規則涵蓋需要抓取頁面
for i in range(1, 17):
    if i == 1:
        htmlname = httphead
    else:
        htmlname = httphead+"?page="+str(i)
    html = urlopen(htmlname)
    # 以BeautifulSoup的"lxml"模式解析網頁，設定為bsObj物件
    bsObj = BeautifulSoup(html, "lxml")
    count = 0
    for single_tr in bsObj.find("table").find("table").findAll("tr")[1:]:  # 抓取網頁資料
        cells = single_tr.findAll(["td"])  # 處理表格中資料
        if search_term in cells[table_index].a.string:
            print(' '.join([cell.a.string or '' for cell in cells]))
