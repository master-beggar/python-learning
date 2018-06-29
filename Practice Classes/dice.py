import random

class Die:
    def __init__(self, sides=2):
        if sides <= 1:
            raise ValueError('You need to choose a die with more than {} sides'.format(size))
        self.value = random.randint(2, sides)

    def __repr__(self):
        return str(self.value)

    def __int__(self):
        return int(self.value)

    def __eq__(self, other):
        return int(self) == other

    def __nq__(self, other):
        return int(self) != other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __le__(self, other):
        return int(self) <= other

    def __ge__(self, other):
        return int(self) >= other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return self + other

class D20(Die):
    def __init__(self, sides = 20):
        super().__init__(sides = sides)

    def __repr__(self):
        return str(self.value)

class Hand(list):
    def __init__(self, size = 0, die_class = D20, *args, **kwargs):
        super().__init__()

        for _ in range(size):
            self.append(die_class())
        self.sort()

    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice
        
    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, size):
        return cls(size = size)

    
