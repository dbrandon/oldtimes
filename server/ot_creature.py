import random
import namegenerator

import base64
from uuid import UUID, uuid4


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

class CreatureStats:
  def __init__(self) -> None:
    self._strength = 0
    self._intellect = 0
    self._endurance = 0

    self._health = 5
    self._mana = 0

  @property
  def strength(self) -> int:
    return self._strength
  @strength.setter
  def strength(self, strength:int):
    self._strength = strength
  
  @property
  def intellect(self) -> int:
    return self._intellect
  @intellect.setter
  def intellect(self, intellect:int):
    self._intellect = intellect

  @property
  def endurance(self) -> int:
    return self._endurance
  @endurance.setter
  def endurance(self, endurance:int):
    self._endurance = endurance

  @property
  def health(self) -> int:
    return self._health
  @health.setter
  def health(self, hp:int):
    self._health = hp
  
  @property
  def mana(self) -> int:
    return self._mana
  @mana.setter
  def mana(self, mp:int):
    self._mana = mp

  def toObj(self):
    return {
      'strength': self.strength,
      'intellect' : self.intellect,
      'endurance' : self.endurance,
      'health': self.health,
      'mana': self.mana,
    }

class Creature:
  def __init__(self, name:str, creature_uuid:UUID) -> None:
    self._name = name
    self._uuid = creature_uuid
    if creature_uuid is None:
      self._uuid = uuid4()

    self._stats = CreatureStats()
    self._inventory = list[Item]()

  def attack(self, other : 'Creature') -> None:
    hit = random.random() > 0.4
    if not hit:
      return self.name + ' swings at ' + other.name + ' but misses!'
    
    damage = int(random.random() * 4)
    if damage < 1:
      return self.name + ' hits ' + other.name + ' with a glancing blow'
    
    health = other.stats.health - damage
    if health < 0:
      health = 0
    other.stats.health = health

    if health < 1:
      return self.name + ' hits ' + other.name + ' for ' + str(damage) + ' points of damage, killing ' + other.name
    return self.name + ' hits ' + other.name + ' for ' + str(damage) + ' points'
  
  
  def is_alive(self) -> bool:
    return self.health > 0
  
  @property
  def name(self) -> str:
    return self._name
  
  @property
  def stats(self) -> CreatureStats:
    return self._stats
  
  @property
  def uuid(self):
    return self._uuid
  
  def toObj(self):
    return {
      'name': self.name,
      'uuid': str(self._uuid.hex),
#      'uuid': str(base64.b64encode(self._uuid.bytes)),
      'stats': self.stats.toObj()
    }
  
