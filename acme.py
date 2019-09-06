import unittest 
import random

class Product(object):
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier= random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
      steal_factor = self.price/self.weight
      if steal_factor < 0.5 :
        return 'Not so stealable'
      elif steal_factor <= 0.5 and steal_factor < 1.0  :
        return 'Kind stealable'
      else :
        return 'Very stealable'
    
    def explode(self):
      explode_f = self.weight * self.flammability
      if explode_f < 10 :
        return '...fizzle'
      elif explode_f >= 10 and explode_f < 50  :
        return '...boom'
      else :
        return 'Very BABOOM'

class BoxingGlove(Product):
    def __init__(self, weight = 10):
        super().__init__(self, weight=weight)
        
    def explode(self):
        return('... its a glove')
          
    def punch(self):
        if self.weight <5 :
            return('that tickels')
          
        elif self.weight >= 5 and self.weight < 15  :
            return('that hurts')
        else:
            return('ouch mother!')