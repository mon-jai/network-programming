from urllib.request import urlopen
from bs4 import BeautifulSoup

htmlname = "https://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0"
html = urlopen(htmlname)
bsObj = BeautifulSoup(html, "lxml")
data = []

search_terms = "年路"

print(bsObj.findAll("div", {"id": "InquiryResule"})[0])

# # 用bsObj物件find找“table”標籤；再找“tbody”標籤 ; 再用findAll找所有"tr"標籤，設定為single_tr物件。
# for single_tr in bsObj.findAll("table")[1].findAll("tr")[1:]:
#     # 對single_tr物件用findAll找所有"td"標籤，設為cell物件
#     cell = single_tr.findAll("td")
#     # 將cell[0]、cell[1]與cell[2]中text取出(編號、英文、中文)組合為data串列
#     if search_terms in cell[2].text:
#         data += [[cell[1].text, cell[1].text, cell[2].text]]

# data.sort(key=lambda item: f'{item[1]} {item[0]}')

# print(data)
