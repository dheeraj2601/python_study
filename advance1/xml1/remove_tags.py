from lxml import etree

tree = etree.parse('testing2.xml')
root = etree.Element("root")

listing = ['dk', 'dk2', 'dheeraj']

for elem in tree.iter():
   print(elem.tag, elem.text)
   if elem.tag in listing:
      parent = elem.getparent()
      parent.remove(elem)

tree.write("testing3.xml", pretty_print=True)
