
from .ot_creature import Creature, random_creature_name
from .ot_monster import Monster
from .ot_party import Party, PartyMember
from .ot_util import OTUtil

import copy
import uuid

class ScenarioRoom:
  def __init__(self) -> None:
    pass
  

class OTScenario:
  def __init__(self, id:uuid.UUID, raw:dict) -> None:
    self._uuid = id
    if raw != None:
      self._name = OTUtil.get_str(raw, 'name')

    self._load_rooms(OTUtil.get_dict(raw, 'room-info'))

    self._monsters = list[Monster]()
    raw_monsters = OTUtil.get_list(raw, 'monsters')
    for raw_monster in raw_monsters:
      self._monsters.append(Monster.fromRaw(raw_monster))

  def _load_rooms(self, raw:dict):
    default_room = OTUtil.get_str(raw, 'default')
    print('default room = ' + default_room)
    self._rooms = list[ScenarioRoom]()

  def clone(self) -> 'OTScenario':
    return copy.deepcopy(self)

  @property
  def id(self) -> uuid.UUID:
    return self._uuid

  @property
  def name(self) -> str:
    return self._name
  
  @property
  def monsters(self) -> list[Monster]:
    return self._monsters
  
  def get_brief(self):
    return {
      'name': self.name,
      'id': self.id
    }

  def getMonstersObj(self):
    monsters = []
    for m in self.monsters:
      monsters.append(m.toObj())
    return monsters


class OTScenarioManager:
  def __init__(self) -> None:
    self._scenario_list = list[OTScenario]()

    print('Load scenarios...')
    for entry in OTUtil.get_scenario_files():
      scen = OTScenario(OTUtil.get_name_as_uuid(entry), OTUtil.load_yaml(entry))
      print('   -> Loaded ' + str(scen.id) + ' with name =[' + scen.name + ']')
      self._scenario_list.append(scen)

  def get_scenario_by_name(self, name:str):
    for s in self._scenario_list:
      if s.name == name:
        return s
    return None


  @property
  def scenario_list(self):
    brief_list = list()
    for s in self._scenario_list:
      brief_list.append(s.get_brief())
    return brief_list
      

class OTScenarioPlayer:
  def __init__(self, scenario: OTScenario, party:Party) -> None:
    self._scenario = scenario
    self._party = party
    self._finished = False

    pass

  def attack(self) -> list[str]:
    result = list[str]()

    if self.is_finished:
      result.append('The scenario is complete.')
      return result
    
    monster = self.scenario.monsters[0]
    result.append(self.party[0].attack(monster))
    if not monster.is_alive:
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
  def scenario(self) -> OTScenario:
    return self._scenario
  
