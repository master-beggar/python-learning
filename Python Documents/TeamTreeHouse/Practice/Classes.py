import webbrowser

class Automobile:
    def __init__(self, make, model, year, *args, **kwargs):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return '{} {} {}'.format(self.year, self.make, self.model)

    def __repr__(self):
        return '{}-{}-{}'.format(self.make, self.model, self.year)

    def __int__(self):
        return int(self.year)

    def distance_traveled(self, distance):
        self.distance = distance

    @property
    def online_search(self):
        webbrowser.open('http://google.com/?#q='+ str(self))

    @classmethod
    def from_string(cls, string):
        string = string.split('-')
        for word in string:
            string[string.index(word)] = word.strip()
        make, model, year = string
        return cls(make, model, year)

car1 = Automobile.from_string('toyota-corolla-2003')
car1.distance_traveled(100)
print(car1)
print(int(car1))
print(car1.distance)
# car1.online_search
