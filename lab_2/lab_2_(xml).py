import xml.dom.minidom as minidom

xml_file = open("currency.xml", 'r')
file = xml_file.read()

dom = minidom.parseString(file)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
namevalue = {}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == "Name":
                if child.firstChild.nodeType == 3:
                    name = child.firstChild.data
            if child.tagName == "Value":
                if child.firstChild.nodeType == 3:
                    value = child.firstChild.data
    namevalue[name] = float(value.replace(',', '.'))


print(namevalue)



xml_file.close()