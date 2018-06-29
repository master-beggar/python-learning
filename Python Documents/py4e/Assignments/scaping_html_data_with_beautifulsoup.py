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

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
sum = 0

for tag in tags:
    count += 1
    print('TAG:', tag)
    print('URL:', tag.get('href',None))
    print('Contents:',int(tag.contents[0]))
    print('Attrs:',tag.attrs)
    sum += int(tag.contents[0])

print('Count:', count)
print('Sum:', sum)
