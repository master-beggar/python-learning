class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.served = 0

    def served(self):
        self.served += self
        return self.served
        
    
class IceCreamParlour(Restaurant):
    def __init__(self, name, cuisine=None):
        flavours = ['apple', 'banana', 'chocolate', 'vanilla']
        super().__init__(name, cuisine)
        self.flavours = flavours

    def __str__(self):
        print('This can not be turned into a string object')

    def __int__(self):
        try:
            return int(self.flavours)
        except TypeError:
            return 1

    def show_flavours(self):
        for num, flavour in enumerate(self.flavours, start = 1):
            print(num, flavour)

    def add_flav(self, flavour):
        return self.flavours.append(flavour)

    def remove_flav(self, flavour):
        return self.flavours.remove(flavour)

    def have_flav(self, flavour):
        return True if flavour in self.flavours else False

    

    
    

    
