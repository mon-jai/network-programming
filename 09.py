from xml.etree.ElementTree import Element, ElementTree

tree = ElementTree(file="cont.xml")
root = tree.getroot()

for country in root:
    if country.attrib["name"] == "新加坡":
        neighbor = Element("neighbor")
        neighbor.attrib["name"] = "亞特蘭提斯"
        neighbor.attrib["direction"] = "南"
        country.append(neighbor)
    elif country.attrib["name"] == "愛爾蘭":
        for country_data in country:
            if country_data.tag == "gdppc":
                country_data.text = "88888"

tree.write("output.xml", encoding="utf-8")
