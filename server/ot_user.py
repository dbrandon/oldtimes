
from flask_login import UserMixin

class OTUser(UserMixin):
  def __init__(self, id, name) -> None:
    self.id = id
    self.name = name
    self.password = self.name + "_secret"

    UserMixin.is_active = True

  def to_json(self):
    return {"name": self.name, "email": self.email}