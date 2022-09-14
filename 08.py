from typing import TypedDict
from xml.etree.ElementTree import ElementTree
import json


class Item(TypedDict):
    name: str
    price: str


class Meal(TypedDict):
    hours: str
    items: dict[str, str]


menu: dict[str, Meal] = {}

tree = ElementTree(file='menu.xml')
root = tree.getroot()

for child in root:
    meal = Meal(hours=child.attrib["hours"], items={})
    for grandchild in child:
        meal["items"][grandchild.text or ""] = grandchild.attrib["price"]
    menu[child.tag] = meal

night_snack = Meal(
    hours="21-23", items={"beer": "$10", "skewers": "$20", "barbecue": "$15"})
menu["Night snack"] = night_snack

with open('menu.json', 'w') as f:
    json.dump(menu, f)
