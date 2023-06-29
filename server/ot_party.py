
from .ot_creature import Creature

class PartyMember(Creature):
  def __init__(self, name: str, cls:str) -> None:
    super().__init__(name)
    self._class = cls
    self.init_stats()

  def init_stats(self) -> None:
    if self._class == 'warrior':
      self.strength = 20
      self.intellect = 5
      self.endurance = 14
    elif self._class == 'cleric':
      self.strength = 12
      self.intellect = 14
      self.endurance = 9
    else:
      raise 'Unknown class: [' + self._class + ']'
    
    self.health = self.endurance * 2
    self.mana = self.intellect

  @property
  def cls(self) -> str:
    return self._class


class Party:
  def __init__(self) -> None:
    self._members: list[PartyMember] = [] 
    pass

  @property
  def members(self) -> list[PartyMember]:
    return self._members