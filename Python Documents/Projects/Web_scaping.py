# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = r'http://py4e-data.dr-chuck.net/comments_42.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
for item in soup('span'):
    count += int(''.join(item.contents))

print(count)


# for tag in soup('a'): #or you could use soup.find_all('a')
#     print(tag.get('href'))
#
# print('-------------')
# print(soup.a)
# print('-------------')
# print(soup.title)
# print('-------------')
# print(soup.title.string.strip())
# print('-------------')
# print(soup.get_text())
# print('-------------')
