import os, numpy as np

# with open('test.txt','r') as f:
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents)

with open('test.txt','r+') as f:
    print(f.name)
    size = 10
    f_contents = f.read(size)
    while len(f_contents)>0:
        print(f_contents, end ='')
        f_contents = f.read(size)

os.chdir(r'C:\users\ahmad walid naimi\desktop')



    # end = f.tell()
    # f.seek(end)
    # f.write('11) This is the eleventh line')
    # f.write('12) this is the last line')
