
from .ot_creature import Creature

class PartyMember(Creature):
  def __init__(self, name: str, cls:str) -> None:
    super().__init__(name)
    self._class = cls
    self.init_stats()

  def init_stats(self) -> None:
    if self._class == 'warrior':
      self.stats.strength = 20
      self.stats.intellect = 5
      self.stats.endurance = 14
    elif self._class == 'cleric':
      self.stats.strength = 12
      self.stats.intellect = 14
      self.stats.endurance = 9
    else:
      raise 'Unknown class: [' + self._class + ']'
    
    self.stats.health = self.stats.endurance * 2
    self.stats.mana = self.stats.intellect

  @property
  def cls(self) -> str:
    return self._class
  
  def toObj(self):
    obj = super().toObj()
    obj['cls'] = self.cls
    return obj


class Party:
  def __init__(self) -> None:
    self._members: list[PartyMember] = [] 
    pass

  @property
  def members(self) -> list[PartyMember]:
    return self._members
  
  def toObj(self):
    jmembers = []
    for m in self.members:
      jmembers.append(m.toObj())
    return { 'members': jmembers }
