#taking control of the built-in classes in python


class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self

print(ReversedStr('hello'))


import copy
class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))

class JSObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            return super().__getattribute__(item)

jso = JSObject({'name':'Walid'})
jso.lang = 'Python'
print(jso.lang)
print(jso.fake)
        

