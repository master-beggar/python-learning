import os

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'romeo.txt'
handle = open(fname)

total = []

for line in handle:
    words = line.split()
    for word in words:
        if word not in total:
            total.append(word)
total.sort()
print(total)
