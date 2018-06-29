import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter Location:')
# url = r'http://py4e-data.dr-chuck.net/comments_42.json'
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieving', url)
# print(data.decode())
tree = json.loads(data)

sum = 0
for item in tree['comments']:
    count_int = int(item['count'])
    sum += count_int
print(sum)
# print('name:', name, 'count:', count)
