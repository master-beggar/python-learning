import random

class Character:
    def __init__(self, name='', **kwargs):
        if not name:
            raise ValueError("'name' is required")
        self.name = name
        
        for key, value in kwargs.items():
            setattr(self, key, value)

class Sneaky:
    def __init__(self, sneaky=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sneaky = sneaky
        
    def hide(self, light_level):
        return self.sneaky and light_level < 10

        
class Agile:
    def __init__(self, agile=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.agile = agile
        
    def evade(self):
        return self.agile and random.randint(0, 1)

class Thief(Agile, Sneaky, Character):
    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
