# from typing import TypedDict
from xml.etree.ElementTree import ElementTree

tree = ElementTree(file='cont.xml')
root = tree.getroot()

for country in root:
    if country.attrib['name'] == '新加坡':
        for country_data in country:
            pass

tree.write("output.xml",encoding="utf-8")