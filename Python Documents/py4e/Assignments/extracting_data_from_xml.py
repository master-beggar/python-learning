import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# url = input('Enter Location:')
url = r'http://py4e-data.dr-chuck.net/comments_76253.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieving', url)
# print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('./comments/comment/count')
# or results = tree.findall('.//count')

sum = 0
for item in results:
    count_int = int(item.text)
    sum += count_int
print(sum)
# print('name:', name, 'count:', count)
