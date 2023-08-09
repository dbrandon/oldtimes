
from .ot_creature import Creature, random_creature_name
from .ot_monster import Monster
from .ot_party import Party, PartyMember
from .ot_util import OTUtil

import copy
import uuid

class OTRoomDefinition:
  def __init__(self, raw:dict) -> None:
    self._name = OTUtil.get_str(raw, 'name')
    enter = OTUtil.get_dict(raw, 'on-enter')
    self._say = OTUtil.get_str(enter, 'say')

    self._hidden_items : list[str] = []

    hidden = OTUtil.get_list(raw, 'hidden')
    for h in hidden:
      item = OTUtil.get_dict(h, 'item')
      desc = OTUtil.get_str(item, 'description')
      self._hidden_items.append(desc)
      print('  Room contains hidden item: ' + desc)

  @property
  def name(self) -> str:
    return self._name
  

class OTScenarioDefinition:
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
    self._rooms = list[OTRoomDefinition]()
    raw_rooms = OTUtil.get_list(raw, 'stages')
    for raw_room in raw_rooms:
      room = OTRoomDefinition(raw_room)
      self._rooms.append(room)
      if room.name == default_room:
        print('Found default room = ' + default_room)
        self._initial_room = room

  def clone(self) -> 'OTScenarioDefinition':
    return copy.deepcopy(self)

  @property
  def id(self) -> uuid.UUID:
    return self._uuid
  
  @property
  def initial_room(self) -> OTRoomDefinition:
    return self._initial_room

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
    self._scenario_list = list[OTScenarioDefinition]()

    print('Load scenarios...')
    for entry in OTUtil.get_scenario_files():
      scen = OTScenarioDefinition(OTUtil.get_name_as_uuid(entry), OTUtil.load_yaml(entry))
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


class OTRoomInstance:
  def __init__(self, room:OTRoomDefinition) -> None:
    self._room = room
    self._initial_enter = True
    self._hidden_items = room._hidden_items.copy()
    self._items : list[str] = []
    pass

  @property
  def name(self) -> str:
    return self._room.name
  
  @property
  def on_enter(self) -> str:
    return self._room._say
  
  def get_actions(self):
    actions = [
      { 'name': 'Look' },
      { 'name': 'Search' }
    ]
    for item in self._items:
      actions.append({ 'name': 'Pick up ' + item})
    return actions
  
  def get_events(self):
    events = []
    if self._initial_enter:
      self._initial_enter = False
      events.append({ 'text': 'The party has entered ' + self.name })
      if self._room._say != '':
        events.append({ 'text': self._room._say })

    return events
  
  def get_status(self):
    return {
      'roomName': self.name,
      'events': self.get_events(),
      'actions': self.get_actions()
    }

  def run_action(self, action: str):
    events = self.get_events()

    if action['name'] == 'Search':
      if len(self._hidden_items) > 0:
        item = self._hidden_items.pop()
        self._items.append(item)
        events.append({ 'text': 'You dig around and find ' + item })
      else:
        events.append({ 'text': 'You search but did not find anything' })
    
    elif action['name'] == 'Look':
      events.append({ 'text': self._room._say })

    return {
      'roomName': self.name,
      'events': events,
      'actions': self.get_actions(),
    }


class OTScenarioInstance:
  def __init__(self, scenario: OTScenarioDefinition, party:Party) -> None:
    self._scenario = scenario
    self._party = party
    self._finished = False
    self._cur_room = OTRoomInstance(scenario.initial_room)
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
  
  def get_status(self):
    return self._cur_room.get_status()
  
  def run_action(self, action):
    return self._cur_room.run_action(action)


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
  def scenario(self) -> OTScenarioDefinition:
    return self._scenario
  
