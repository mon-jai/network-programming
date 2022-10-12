from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlname = "https://www.cwb.gov.tw/V8/C/K/bilingual_glossary.html"
html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
# 用bsObj物件find找"table"標籤；再找"thead"標籤；再找"tr"標籤，再用findAll找所有"th"標籤，並設為cell物件。
cell = bsObj.find("table").find("thead").find("tr").findAll("th")
data = []

# 用bsObj物件find找“table”標籤；再找“tbody”標籤 ; 再用findAll找所有"tr"標籤，設定為single_tr物件。
for single_tr in bsObj.find("table").find("tbody").findAll("tr"):
    # 對single_tr物件用findAll找所有"td"標籤，設為cell物件
    cell = single_tr.findAll("td")
    # 將cell[0]、cell[1]與cell[2]中text取出(編號、英文、中文)組合為data串列
    F1 = cell[1].text
    F2 = cell[2].text
    data += [[F1, F2]]

word = input()

for english_vocab, chinese_vocab in data:
    if word in chinese_vocab:
        print(f'{chinese_vocab} {english_vocab}')
    elif word in english_vocab:
        print(f'{english_vocab} {chinese_vocab}')
