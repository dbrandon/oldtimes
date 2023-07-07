
import os
import uuid
import yaml

OT_BASE_DIR = 'data'
OT_SCENARIO_DIR = os.path.join(OT_BASE_DIR, 'scenarios')

class OTUtil:
  def get_str(d: dict, field_name: str, def_value: str = None, raise_on_none: bool = True) -> str:
    v = d.get(field_name)
    if v == None and def_value == None and raise_on_none:
      raise LookupError('Missing field \'' + field_name + '\'')
    return str(v) if v != None else def_value

  def get_bool(d: dict, field_name: str, def_value: bool = None) -> bool:
    v = d.get(field_name)
    return bool(v) if v != None else def_value

  def get_int(d:dict, field_name: str, def_value: int = None, raise_on_none: bool = True) -> int:
    v = d.get(field_name)
    if v == None and def_value == None and raise_on_none:
      raise LookupError('Missing field \'' + field_name + '\'')
    return int(v) if v != None else def_value

  def get_list(d: dict, field_name: str, empty_list_if_none: bool = True) -> list:
    v = d.get(field_name)
    if v != None and not isinstance(v, list):
      raise LookupError('Field \'' + field_name + '\' is not a list')
    if v == None and empty_list_if_none:
      v = []
    return v

  def get_type_id(x) -> str:
    if x == None:
      raise LookupError('get_type_id: argument was None')
    if isinstance(x, dict):
      type_id = x.get('type_id')
      if type_id == None:
        raise LookupError('get_type_id: missing field type_id')
      return str(type_id)
    if isinstance(x, str):
      return x
    if isinstance(x, int):
      return str(x)
    raise LookupError('get_type_id: Unable to lookup id from type ' + str(type(x)))
  
  def get_basename(filename:str) -> str:
    return os.path.basename(filename)
  
  def get_name_as_uuid(filename:str) -> uuid.UUID:
    base = OTUtil.get_basename(filename)
    uuid_text = os.path.splitext(base)[0]
    return uuid.UUID(uuid_text)


  def get_scenario_files():
    filez = list[str]()
    for file in os.listdir(OT_SCENARIO_DIR):
      filez.append(os.path.join(OT_SCENARIO_DIR, file))
    return filez

  def load_yaml(filename: str):
    with open(filename) as f:
      return yaml.safe_load(f)