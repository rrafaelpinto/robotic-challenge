from enum import Enum

class Stack(Enum):
    REJECTED = "REJECTED"
    SPECIAL = "SPECIAL"
    PRIORITY = "PRIORITY"
    FRAGILE = "FRAGILE"
    STANDARD = "STANDARD"

class Package:

    BULKY_VOLUME = 1000000
    BULKY_DIMENSION = 150
    HEAVY_MASS = 20
    FRAGILE_VOLUME = 100
    HIGH_PRIORITY_VOLUME = 500
    HIGH_PRIORITY_MASS = 10

    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    @property
    def volume(self):
        return (self.width * self.height * self.length)

    def is_bulky(self):
        return ((self.volume >= Package.BULKY_VOLUME) or (self.width >= Package.BULKY_DIMENSION or self.height >= Package.BULKY_DIMENSION or self.length >= Package.BULKY_DIMENSION))

    def is_fragile(self):
        return (self.volume <= Package.FRAGILE_VOLUME)
    
    def is_high_priority(self):
        return (self.mass >= Package.HIGH_PRIORITY_MASS and self.volume <= Package.HIGH_PRIORITY_VOLUME)

    def is_heavy(self):
        return (self.mass >= Package.HEAVY_MASS)


    def get_stack(self):
        rules = [
            (self.is_bulky() and self.is_heavy(), Stack.REJECTED.value),
            (self.is_bulky() or self.is_heavy(), Stack.SPECIAL.value),
            (self.is_high_priority(), Stack.PRIORITY.value),
            (self.is_fragile(), Stack.FRAGILE.value),            
        ]
        for condition, stack in rules:
            if condition:
                return stack
        return Stack.STANDARD.value