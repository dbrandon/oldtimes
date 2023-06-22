
from flask_login import UserMixin
from .ot_scenario import OTScenario

class OTUser(UserMixin):
  def __init__(self, id, name) -> None:
    self.id = id
    self._name = name
    self.password = self._name + "_secret"
    self._scenario = None

    UserMixin.is_active = True

  @property
  def name(self) -> str:
    return self._name

  def to_json(self):
    return {"name": self.name, "email": self.email}
  
  @property
  def scenario(self) -> OTScenario:
    return self._scenario
  
  def get_scenario(self) -> OTScenario:
    return self._scenario
  
  def set_scenario(self, scenario:OTScenario) -> None:
    self._scenario = scenario