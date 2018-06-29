import random
import webbrowser
import os

fname = r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\Projects\pornstars.txt'

actress = {}
for line in open(fname):
    line = line.split('-')
    for word in line:
        line[line.index(word)] = word.strip()
        print(line)
    # actress[line[0]] = line[1]


category = []
for k,v in actress.items():
    if v not in category:
        category.append(v)

typeof = random.choice(category)

names = []
for k,v in actress.items():
    if v == typeof.lower():
        names.append(k)

if typeof == "asian":
    webbrowser.open('http://javfor.me/?s=' + random.choice(names),new=2)
elif typeof == "white":
    webbrowser.open('https://www.ceporn.net/search.html?q=' + random.choice(names),new=2)
else:
    print("Then find something on your own")
