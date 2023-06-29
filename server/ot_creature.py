import random
import namegenerator


class Item:
  def __init__(self, name:str) -> None:
    self._name = name

  @property
  def name(self) -> str:
    return self._name

def random_creature_name() -> str:
  first_name = random.choice(namegenerator.LEFT).capitalize()
  last_name = random.choice(namegenerator.RIGHT).capitalize()
  return first_name + ' ' + last_name

class Creature:
  def __init__(self, name:str) -> None:
    self._name = name
    self._stats = dict[str,int]()
    self._var = dict[str,int]()
    self._inventory = list[Item]()

    self.health = 5
    self.mana = 0

  def attack(self, other : 'Creature') -> None:
    hit = random.random() > 0.4
    if not hit:
      return self.name + ' swings at ' + other.name + ' but misses!'
    
    damage = int(random.random() * 4)
    if damage < 1:
      return self.name + ' hits ' + other.name + ' with a glancing blow'
    
    health = other.health - damage
    if health < 0:
      health = 0
    other.health = health

    if health < 1:
      return self.name + ' hits ' + other.name + ' for ' + str(damage) + ' points of damage, killing ' + other.name
    return self.name + ' hits ' + other.name + ' for ' + str(damage) + ' points'
  
  @property
  def strength(self) -> int:
    return self._stats['str']
  
  @strength.setter
  def strength(self, strength:int):
    self._stats['str'] = strength
  
  @property
  def intellect(self) -> int:
    return self._stats['int']
  @intellect.setter
  def intellect(self, intellect:int):
    self._stats['int'] = intellect

  @property
  def endurance(self) -> int:
    return self._stats['end']
  @endurance.setter
  def endurance(self, endurance:int):
    self._stats['end'] = endurance
  
  @property
  def is_alive(self) -> bool:
    return self.health > 0
  
  @property
  def name(self) -> str:
    return self._name
  
  @property
  def health(self) -> int:
    return self._var['hp']
  
  @health.setter
  def health(self, hp:int):
    self._var['hp'] = hp
  
  @property
  def mana(self) -> int:
    return self._var['mp']
  
  @mana.setter
  def mana(self, mp:int):
    self._var['mp'] = mp
