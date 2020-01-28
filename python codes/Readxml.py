import xml.etree.ElementTree as ET

tree= ET.parse('clusterconfig.xml')

root = tree.getroot()


for child in root:
    if child.tag=='uri':
        uri=child.text
    else:
        for element in child:
            host=element.text

print('uri:'+uri)
print('host:'+host)

