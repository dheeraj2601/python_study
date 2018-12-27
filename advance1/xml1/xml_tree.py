# print xml in tree form

import re, collections
from lxml import etree


xml_root = etree.parse("testing.xml").getroot()


#xml_root = etree.tostring(xml)
raw_tree = etree.ElementTree(xml_root)
nice_tree = collections.OrderedDict()

for tag in xml_root.iter():
    path = re.sub('\[[0-9]+\]', '', raw_tree.getpath(tag))
    if path not in nice_tree:
        nice_tree[path] = []
    if len(tag.keys()) > 0:
        nice_tree[path].extend(attrib for attrib in tag.keys() if attrib not in nice_tree[path])

for path, attribs in nice_tree.items():
    indent = int(path.count('/'))
    print('{0}{1}: {2}'.format('    ' * indent, indent, path.split('/')[-1]))
~                                                                                       
