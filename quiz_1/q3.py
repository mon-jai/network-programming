from urllib.request import urlretrieve
from xml.etree.ElementTree import SubElement, ElementTree, Element

xmlFileName = "data1.xml"
outputFileName = "data2.xml"

urlretrieve(
    'https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/xml/preview',
    filename=xmlFileName
)

tree = ElementTree(file=xmlFileName)
root = tree.getroot()

row = SubElement(root, "row")

sno = SubElement(row, "sno")
sna = SubElement(row, "sna")
tot = SubElement(row, "tot")
sbi = SubElement(row, "sbi")
sarea = SubElement(row, "sarea")

sno.text = "1033"
sna.text = "家樂福新店店"
tot.text = "30"
sbi.text = "29"
sarea.text = "新店區"

for shop in root:
    shop_to_modify = False

    for shop_data in shop:
        if shop_data.tag == "sno" and shop_data.text == "1018":
            shop_to_modify = True
        else:
            break

    if shop_to_modify == True:
        for shop_data in shop:
            if shop_data.tag == "sbi":
                shop_data.text = '0'

tree.write(outputFileName, encoding="utf-8")

tree_2 = ElementTree(file=outputFileName)
root_2 = tree.getroot()

print('sno sna tot sbi')

for shop in root_2:
    shop_to_print = False

    for shop_data in shop:
        if shop_data.tag == "sarea" and shop_data.text == "新店區":
            shop_to_print = True

    if shop_to_print == True:
        for shop_data in shop:
            if shop_data.tag in ["sno", "sna", "tot", "sbi"]:
                print(shop_data.text, end=' ')
        print('')
