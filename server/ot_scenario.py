
from .ot_creature import Creature, random_creature_name
from .ot_party import Party, PartyMember

      

class Monster(Creature):
  def __init__(self, name: str, kind:int) -> None:
    super().__init__(name)
    self._kind = kind
    self.init_stats()

  def init_stats(self):
    self.strength = 18
    self.intellect = 2
    self.endurance = 8
    self.health = 15
    

class OTScenario:
  def __init__(self, name:str, party:Party) -> None:
    self._name = name
    self._party = party

    if self._party == None:
      self._party = OTScenario.create_party()

    self._monsters = list[Monster]()
    self._monsters.append(Monster(random_creature_name(), 1))

    self._finished = False

    pass

  def create_party() -> Party:
    party = Party()

    party.members.append(PartyMember(random_creature_name(), 'warrior'))
    party.members.append(PartyMember(random_creature_name(), 'cleric'))
    return party

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
    return self._party.members
  
  @property
  def monsters(self) -> list[Monster]:
    return self._monsters