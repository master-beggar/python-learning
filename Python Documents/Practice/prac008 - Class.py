class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __int__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self.value) + other
        else:
            return int(self.value) + other

    def __radd__(self, other):
        return self + other

    def _iadd__(self, other):
        self.value = self + other
        return self.value

class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.add(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        # for item in self.slots:
        #     yield item
        yield from self.slots

class ReversedStr(str):
    # returns the input string backwards
    def __new__(*args, **kwargs):
        rev = str.__new__(*args, **kwargs)
        rev = rev[::-1]
        return rev

class Rectangle:

    def __init__(self,length, width):
        self.lenght = length
        self.width = width
        self.__name = 'easter egg' #can't be changed by call from instance

    @property #you don't have to include '()' for the method when it is a property; a property can't be set either
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return (self.length*2 + self.width*2)

def roman():
    num = int(input('Type a number and I will return a roman numeral for it: '))
    static_num = num
    roman = ''
    roman_call = [(1000, 'M'), (500, 'D'), (100, 'C'), (50,'L'), (40, 'XL'), (10,'X'), (9, 'IX'), (5,'V'), (4,'IV'), (1,'I')]

    for i,r in roman_call:
        while num >= i:
            roman += r
            num -= i
    return static_num, roman

num, roman = roman()
print('The roman numeral for {} is: {}'.format(num,roman))
