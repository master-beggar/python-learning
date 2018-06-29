import os

os.chdir(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\py4e')

fname = 'mbox-short.txt'
handle = open(fname)

counts = dict()

for line in handle:
    words = line.split()
    if line.startswith('From') and len(words)>2:
        email = words[1]
        domain = email.split('@')[1]
        counts[domain] = counts.get(domain,0)+1

print(counts)


# bigcount = None
# bigword = None
#
# for k,v in counts.items():
#     if bigcount is None or v > bigcount:
#         bigword = k
#         bigcount = v
#
# print(bigword, bigcount)
