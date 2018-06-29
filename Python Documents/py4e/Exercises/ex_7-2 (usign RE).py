import os
import re

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

numbers = []

for line in handle:
    number = re.findall('X-DSPAM-Confidence: ([0-9.]+)',line)
    if len(number) > 0:
        number = float(number[0])
        numbers.append(number)
aver = sum(numbers)/len(numbers)
print('Average spam confidence:',aver)
