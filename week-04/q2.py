from __future__ import unicode_literals, print_function
import urllib
from bs4 import BeautifulSoup
import urllib.request
request_url = 'http://invoice.etax.nat.gov.tw/'  # 財政部官網
htmlContent = urllib.request.urlopen(request_url).read()  # 開啟網址取得HTML
soup = BeautifulSoup(htmlContent, "html.parser")  # 以"html.parser"解析設為soup物件
# 用soup的find_all找網頁所有標籤為"span"且class屬性值為"font-weight-bold etw-color-red"與"font-weight-bold"的內容,設給result物件
results = soup.find_all(
    "span", {"class": {"font-weight-bold etw-color-red", "font-weight-bold"}})

winning_numbers_endings = [
    f'{results[index].text}' for index in range(3, 8, 2)]

invoice_number = input()[4:]

if invoice_number in winning_numbers_endings:
    print('中二百元')
elif max(
    sum(
        1 for index, character in enumerate(invoice_number)
        if character == winning_numbers_ending[index]
    )
    for winning_numbers_ending in winning_numbers_endings
) == 2:
    print('差一個號碼中兩百元')
