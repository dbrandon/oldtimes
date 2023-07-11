
from .ot_creature import Creature, CreatureStats
from .ot_util import OTUtil

class Monster(Creature):
  def __init__(self, name: str, kind:int, stats:CreatureStats = None) -> None:
    super().__init__(name, None, stats)
    self._kind = kind
    if stats == None:
      self.init_stats()

  def fromRaw(raw:dict) -> 'Monster':
    name = OTUtil.get_str(raw, 'name')
    kind = OTUtil.get_str(raw, 'kind')
    raw_stats = OTUtil.get_dict(raw, 'stats')
    stats = CreatureStats(raw_stats)
    return Monster(name, kind, stats)

  def init_stats(self):
    self.stats.strength = 18
    self.stats.intellect = 2
    self.stats.endurance = 8
    self.stats.health = 15

  def toObj(self):
    obj = super().toObj()
    obj['kind'] = 'Big Meanie'
    return obj
    

