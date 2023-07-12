
from flask_login import UserMixin
from .ot_party import Party
from .ot_scenario import OTScenarioInstance

class OTUser(UserMixin):
  def __init__(self, id, name) -> None:
    self.id = id
    self._name = name
    self.password = self._name + "_secret"
    self._party = None
    self.scenario_instance = None

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
  def scenario_instance(self) -> OTScenarioInstance:
    return self._scenario_instance
  
  @scenario_instance.setter
  def scenario_instance(self, scenario_instance:OTScenarioInstance) -> None:
    self._scenario_instance = scenario_instance