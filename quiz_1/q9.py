import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

response = requests.get("https://www.etax.nat.gov.tw/etw-main/ETW183W2_11101/")
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "lxml")

special_prize_number = ""
first_prize_number = ""
grand_prize_number = ""

table = soup.find(id="tenMillionsTable")
assert isinstance(table, Tag)

for tr in table.find_all("tr"):
    th = tr.find("th")

    if th == None:
        continue

    heading = th.text

    if heading == "特別獎":
        special_prize_number = tr.find(class_="row").text.strip()
    elif heading == "特獎":
        first_prize_number = tr.find(class_="row").text.strip()
    elif heading == "頭獎":
        grand_prize_number = tr.find(class_="row").text.split()
