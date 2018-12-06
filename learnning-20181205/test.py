import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
# root = tree.getroot()

# 根据字符串解析
# root = ET.fromstring('<data></data>')
# 获取tag名称
# print(root.tag)
# 获取属性
# print(root.attrib)

# 循环子节点
# for child in root:
#     print(child.tag, child.attrib)

# 根据下标找到节点，从0开始
# print(root[0][1].text)

# Pull API用于非阻塞解析
# parser = ET.XMLPullParser(['start', 'end'])
# parser.feed("<mytag>sometext")
# print(list(parser.read_events()))
# parser.feed(' more text</mytag>')
# for event, elem in parser.read_events():
#     print(event)
#     print(elem.tag, 'text=', elem.text)

# 遍历所有节点名为neighbor
# for neighbor in root.iter('neighbor'):
#     print(neighbor.attrib)

# Element.findall()仅查找具有标记的元素，这些元素是当前元素的直接子元素。
# Element.find()查找具有特定标记的第一个子项，并Element.text访问该元素的文本内容。
# Element.get()访问元素的属性
# for country in root.findall('country'):
#     rank = country.find('rank').text
#     name = country.get('name')
#     print(name, rank)

# ElementTree提供了一种构建XML文档并将其写入文件的简单方法。该ElementTree.write()方法用于此目的。
# 一旦创建，Element可以通过直接更改其字段（例如Element.text），添加和修改属性（Element.set()方法）以及添加新子项（例如with Element.append()）来操纵对象。
# 假设我们想在每个国家/地区的排名中添加一个，并updated 在rank元素中添加一个属性
# for rank in root.iter('rank'):
#     new_rank = int(rank.text) + 1
#     rank.text = str(new_rank)
#     rank.set('updated', 'yes')
# tree.write('output.xml')

# 我们可以使用删除元素Element.remove()。假设我们要删除排名高于50的所有国家/地区
# for country in root.findall('country'):
#     rank = int(country.find('rank').text)
#     if rank > 50:
#         root.remove(country)
# tree.write('output.xml')

# SubElement()创建子元素
# a = ET.Element('a')
# b = ET.SubElement(a, 'b')
# c = ET.SubElement(a, 'c')
# d = ET.SubElement(c, 'd')
# ET.dump(a)

# xmlns：默认命名空间 xmlns:fictional 前缀为fictional的命名空间
# root = ET.fromstring("""<?xml version="1.0"?>
#                         <actors xmlns:fictional="http://characters.example.com"
#                                 xmlns="http://people.example.com">
#                             <actor>
#                                 <name>John Cleese</name>
#                                 <fictional:character>Lancelot</fictional:character>
#                                 <fictional:character>Archie Leach</fictional:character>
#                             </actor>
#                             <actor>
#                                 <name>Eric Idle</name>
#                                 <fictional:character>Sir Robin</fictional:character>
#                                 <fictional:character>Gunther</fictional:character>
#                                 <fictional:character>Commander Clement</fictional:character>
#                             </actor>
#                         </actors>""")
# for actor in root.findall('{http://people.example.com}actor'):
#     name = actor.find('{http://people.example.com}name')
#     print(name.text)
#     for char in actor.findall('{http://characters.example.com}character'):
#         print(' |-->', char.text)
# 给命名空间创建字典
# ns = {'real_person': 'http://people.example.com',
#       'role': 'http://characters.example.com'}
# for actor in root.findall('real_person:actor', ns):
#     name = actor.find('real_person:name', ns)
#     print(name.text)
#     for char in actor.findall('role:character', ns):
#         print(' |-->', char.text)
