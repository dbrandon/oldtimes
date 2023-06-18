
from .ot_user import OTUser

import uuid
import namegenerator
import random

class UserManager:
  def __init__(self) -> None:
    self.user_dict = {}

  def establish_user(self):
    id = str(uuid.uuid1())
    first_name = random.choice(namegenerator.LEFT).capitalize()
    last_name = random.choice(namegenerator.RIGHT).capitalize()
    name = first_name + ' ' + last_name
    user = OTUser(id, name)
    self.user_dict[id] = user
    print('Inserting new user with ID = ' + id)
    return user
  
  def lookup_user(self, user_id):
    print('UserManager: request for user ' + user_id)
    user = self.user_dict.get(str(user_id))
    if user == None:
      print('  No user found.')
    return user