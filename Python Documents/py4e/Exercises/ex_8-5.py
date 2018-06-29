import os

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

count = 0

for line in handle:
    if line.startswith('From'):
        words = line.split()
        sender = words[1]
        count = count + 1
    else:
        continue
    print(sender)
print('There were', str(count), 'lines in the file with From as the first word')
