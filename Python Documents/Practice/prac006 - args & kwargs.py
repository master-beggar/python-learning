def func1(*args):
    z = 1
    for arg in args:
        z *= arg
    return z

def func2(**kwargs):
    for key, item in kwargs.items():
        print(key,item)

func2(name='walid',height=1.73,ethnicity='afghan')
