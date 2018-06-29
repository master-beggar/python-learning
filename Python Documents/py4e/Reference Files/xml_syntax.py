import xml.etree.ElementTree as ET

#sample xml formatted data
data = '''
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

# use the fromstring method to parse the data correctly into an object, root
root = ET.fromstring(data)

# As an Element, root has a tag and a dictionary of attributes:
print(root.tag)
print(root.attrib)

# It also has children nodes over which we can iterate:
for child in root:
    print(child.tag, child.attrib)

# Children are nested, and we can access specific child nodes by index:
print(root[0][1].text)

# Element has some useful methods that help iterate recursively over all the
# sub-tree below it (its children, their children, and so on). For example, Element.iter():
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

# Element.findall() finds only elements with a tag which are direct children
# of the current element. Element.find() finds the first child with a particular
# tag, and Element.text accesses the element’s text content. Element.get() accesses
# the element’s attributes:
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)


#XPATH SUPPORT
print('\n','XPATH SUPPORT','\n')
# Top-level elements
root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
root.findall(".//neighbor[2]")
