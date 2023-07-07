
from flask_login import UserMixin
from .ot_party import Party
from .ot_scenario import OTScenarioPlayer

class OTUser(UserMixin):
  def __init__(self, id, name) -> None:
    self.id = id
    self._name = name
    self.password = self._name + "_secret"
    self._party = None
    self._scenario_player = None

    UserMixin.is_active = True

  @property
  def name(self) -> str:
    return self._name

  def to_json(self):
    return {"name": self.name, "email": self.email}
  
  @property
  def party(self) -> Party:
    return self._party
  @party.setter
  def party(self, party:Party):
    self._party = party
  
  @property
  def scenario_player(self) -> OTScenarioPlayer:
    return self._scenario_player
  
  @scenario_player.setter
  def scenario_player(self, scenario_player:OTScenarioPlayer) -> None:
    self._scenario_player = scenario_player