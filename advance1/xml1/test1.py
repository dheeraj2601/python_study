from xml.etree import ElementTree as et
import os

tree = et.parse('abc.xml')

print (tree)
print (tree.getroot())

root1 = tree.getroot()

str_xml = str(tree)
print (root1)
print (root1.tag)
print (root1.attrib)

for child in root1:
    print(child.tag, child.attrib)

