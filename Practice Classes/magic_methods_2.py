#magic method 2

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)

class Weapon(Item):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power

class Inventory:
    def __init__(self):
        self.slots =[]

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self):
        return item in self.slots

    def __iter__(self):
        yield from self.slots

    
