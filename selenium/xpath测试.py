from lxml import etree

# 解析文档
tree = etree.parse('1.xml')
# print(type(tree))
res = tree.xpath('//desc[@class="d1"]/..') # 两个斜杠穿透任一层----@是取属性------------两个..选择父节点
# res = tree.xpath('/site//desc[@class="d1"]/text()') # 两个斜杠穿透任一层----@是取属性
# res = tree.xpath('/site//desc[@*]') # 两个斜杠穿透任一层----@是取属性
# res = tree.xpath('/site//desc/text()') # 获取文本
# res = tree.xpath('/site/book/desc')
# res = tree.xpath('/site/*')
# res = tree.xpath('/site/node()')
print(res)