
import namegenerator
import random

class Item:
  def __init__(self, name:str) -> None:
    self._name = name

  @property
  def name(self) -> str:
    return self._name
  

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
      

class Monster(Creature):
  def __init__(self, name: str, kind:int) -> None:
    super().__init__(name)
    self._kind = kind
    self.init_stats()

  def init_stats(self):
    self.health = 15


class PartyMember(Creature):
  def __init__(self, name: str, cls:str) -> None:
    super().__init__(name)
    self._class = cls
    self.init_stats()

  def init_stats(self) -> None:
    if self._class == 'warrior':
      self._stats['str'] = 20
      self._stats['int'] =  5
      self._stats['end'] = 14
    elif self._class == 'cleric':
      self._stats['str'] = 12
      self._stats['int'] = 14
      self._stats['end'] =  9
    else:
      raise 'Unknown class: [' + self._class + ']'
    
    self.health = self._stats['end'] * 2
    self.mana = self._stats['int']

  @property
  def cls(self) -> str:
    return self._class
    

class OTScenario:
  def __init__(self, name:str) -> None:
    self._name = name
    self._party = OTScenario.create_party()

    self._monsters = list[Monster]()
    self._monsters.append(Monster(OTScenario.create_name(), 1))

    self._finished = False

    pass

  def create_party() -> list[PartyMember]:
    party = list[PartyMember]()

    party.append(PartyMember(OTScenario.create_name(), 'warrior'))
    party.append(PartyMember(OTScenario.create_name(), 'cleric'))
    return party

  def create_name() -> str:
    first_name = random.choice(namegenerator.LEFT).capitalize()
    last_name = random.choice(namegenerator.RIGHT).capitalize()
    return first_name + ' ' + last_name
  
  def attack(self) -> list[str]:
    result = list[str]()

    if not self.monsters[0].is_alive:
      result.append('There are no monsters left to kill!')
      return result
    
    result.append(self.party[0].attack(self.monsters[0]))
    if not self.monsters[0].is_alive:
      result.append('All opponents have been vanquished!')
      self._finished = True
    return result

  @property
  def is_finished(self) -> bool:
    return self._finished

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def party(self) -> list[PartyMember]:
    return self._party
  
  @property
  def monsters(self) -> list[Monster]:
    return self._monsters