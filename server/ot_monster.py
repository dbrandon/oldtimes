
from .ot_creature import Creature

class Monster(Creature):
  def __init__(self, name: str, kind:int) -> None:
    super().__init__(name, None)
    self._kind = kind
    self.init_stats()

  def init_stats(self):
    self.stats.strength = 18
    self.stats.intellect = 2
    self.stats.endurance = 8
    self.stats.health = 15

  def toObj(self):
    obj = super().toObj()
    obj['kind'] = 'Big Meanie'
    return obj
    

