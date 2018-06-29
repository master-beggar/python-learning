import os

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

counts = dict()

for line in handle:
    line = line.rstrip()
    for letter in line:
        letter = letter.lower()
        if letter.isalpha():
            counts[letter] = counts.get(letter,0)+1

sortedlist = sorted([(v,k) for k,v in counts.items()],reverse=True)

for v,k in sortedlist:
    print(k,v)
