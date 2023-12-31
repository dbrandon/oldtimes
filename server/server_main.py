
from flask import Flask, redirect, url_for, render_template, flash, request, jsonify
from flask_login import LoginManager
#from flask_restful import Resource, Api

import flask_login

from .ot_user_manager import UserManager
from .ot_user import OTUser
from .ot_creature import random_creature_name
from .ot_party import Party, PartyMember
from .ot_scenario import OTScenarioInstance, OTScenarioManager

import copy
import os
import sys
import json

OTRoot = os.getcwd()

print('Loading scenarios...')
scenario_manager = OTScenarioManager()

print('Initializing Old Times server...')
Old_Times_Version = 1
OTApp = Flask(__name__, static_url_path = '', static_folder=OTRoot + '/static_html', template_folder=OTRoot + '/templates')
OTApp.config['TEMPLATES_AUTO_RELOAD'] = True

OTApp.secret_key = 'secret key'
OTLoginManager = LoginManager()
OTLoginManager.init_app(OTApp)

@OTApp.route('/rest/hello')
@flask_login.login_required
def rest_hello():
  user = get_user()
  sname = 'None'
  if user.scenario != None:
    sname = user.scenario.name

  return jsonify({ 'username': user.name, 'scen_name' : sname})


heroes = [
    { 'id': 11, 'name': 'Nobody' },
    { 'id': 12, 'name': 'Dr. Nice' },
    { 'id': 13, 'name': 'Bombasto' },
    { 'id': 14, 'name': 'Mr. Weber' },
]

@OTApp.route('/rest/heroes')
@flask_login.login_required
def rest_get_heroes():
  return jsonify({ 'heroes': heroes })

@OTApp.route('/rest/hero/<int:id>', methods=['GET'])
def rest_get_hero(id:int):
  for hero in heroes:
    if hero['id'] == id:
      return jsonify(hero)
    
@OTApp.route('/rest/hero', methods=['POST'])
def rest_add_hero():
  hname = request.data.decode()
  id : int = 1
  for hero in heroes:
    hid = hero['id']
    id = hid+1
  heroes.append( { 'id': id, 'name': hname })
  return jsonify({'ok': True})
    
@OTApp.route('/rest/hero', methods=['PUT'])
def rest_update_hero():
  hero = json.loads(request.data)
  for i in range(len(heroes)):
    if heroes[i]['id'] == hero['id']:
      heroes[i] = hero
      return jsonify({'ok': True})
  return jsonify({'ok': False})

@OTApp.route('/rest/hero/<int:id>', methods=['DELETE'])
def rest_delete_hero(id: int):
  for i in range(len(heroes)):
    if heroes[i]['id'] == id:
      heroes.remove(heroes[i])
      return jsonify({'ok': True})
  return jsonify({'ok': False})


@OTApp.route('/rest/party')
@flask_login.login_required
def rest_get_party():
  user = get_user()
  if user.party == None:
    party = Party()
    party.members.append(PartyMember(random_creature_name(), 'warrior'))
    party.members.append(PartyMember(random_creature_name(), 'cleric'))
    user.party = party
  return jsonify({'ok': True, 'party': user.party.toObj()})

@OTApp.route('/rest/party', methods=['POST'])
@flask_login.login_required
def rest_add_to_party():
  user = get_user()
  member: PartyMember = json.loads(request.data)
  if user.party == None:
    user.party = Party()
  user.party.members.append(member)



@OTApp.route('/rest/scenario/list')
def rest_get_scenario_list():
  return jsonify({'ok': True, 'scenarioList': scenario_manager.scenario_list})

@OTApp.route('/rest/scenario/start', methods=['PUT'])
@flask_login.login_required
def rest_put_scenario_start():
  user = get_user()
  req = json.loads(request.data)
  print('scenario name=[' + req['name'] + ']')
  scenario = copy.deepcopy(scenario_manager.get_scenario_by_name(req['name']))

  user._scenario_instance = OTScenarioInstance(scenario, user.party)
  return jsonify({'ok': True})


@OTApp.route('/rest/scenario/status')
@flask_login.login_required
def rest_get_scenario_status():
  user = get_user()
  return jsonify({'ok': True, 'status': user._scenario_instance.get_status()})

@OTApp.route('/rest/scenario/action', methods=['PUT'])
@flask_login.login_required
def rest_put_scenario_action():
  user = get_user()
  req = json.loads(request.data)
  return jsonify({'ok': True, 'status': user.scenario_instance.run_action(req)})


@OTApp.route('/rest/scenario/monsters')
@flask_login.login_required
def rest_get_secnario_monsters():
  user = get_user()
  return jsonify({'ok': True, 'monsterList': user._scenario_instance.scenario.getMonstersObj()})

@OTApp.route('/rest/scenario/attack')
@flask_login.login_required
def rest_scenario_attack():
  user = get_user()
  return jsonify({'ok': True, 'messageList': user._scenario_instance.attack()})

OTUserManager = UserManager()

@OTLoginManager.user_loader
def load_user(user_id):
    return OTUserManager.lookup_user(user_id)

@OTApp.route('/')
@flask_login.login_required
def get_home_page():
  user = get_user()
  flash('Welcome ' + user.name + '!  Prepare to die!')

  return render_template('start_page.html', version = Old_Times_Version)

@OTApp.route('/begin_game')
@flask_login.login_required
def begin_game():
  user = get_user()

  if user.scenario == None:
    print('Need to start a scenario!')
    user.set_scenario(OTScenario('First Scenario'))
  else:
    print('Scenario already established')
  sys.stdout.flush()
  return render_template('begin_game.html', name = user.name, scenario = user.scenario)

@OTApp.route('/attack')
@flask_login.login_required
def party_attack():
  user = get_user()

  if user.scenario == None:
    flash('No scenario has been started!')
    return redirect(url_for('get_home_page'))
  
  result = user.scenario.attack()
  for msg in result:
    flash(msg)
  return render_template('begin_game.html', name= user.name, scenario = user.scenario)

@OTApp.route('/reset_scenario')
@flask_login.login_required
def reset_scenario():
  user = get_user()
  user.set_scenario(None)
  return redirect(url_for('get_home_page'))

@OTApp.route('/rest/get_authorized')
def rest_get_authorized():
  user = get_user()

  if flask_login.current_user.is_authenticated != True:
    user = OTUserManager.establish_user()
    flask_login.login_user(user)
  return jsonify({'username': user.name})

@OTApp.route('/get_authorized')
def get_authorized():
  print('Request authorization!')
  print(flask_login.current_user)

  if flask_login.current_user.is_authenticated != True:
    user = OTUserManager.establish_user()
    flask_login.login_user(user)
    print('User: ID=' + flask_login.current_user.get_id() + ', Auth=' + str(flask_login.current_user.is_authenticated) + ', Name=' + flask_login.current_user.name)
    flash('You didn\'t provide a name.  I think I\'ll call you... ' + flask_login.current_user.name)
  else:
    print('Already authorized, redirecting ' + flask_login.current_user.name + ' to authtest')
    sys.stdout.flush()
    return redirect(url_for('get_home_page'))
  
  next = request.args.get('next')
  print('next is [' + str(next) + ']')
  sys.stdout.flush()
  return redirect(next or url_for('get_home_page'))

def get_user() -> OTUser:
  return flask_login.current_user

@OTLoginManager.unauthorized_handler
def unauthorized_handler():
  print('login unauthorized!')
  return redirect(url_for('get_authorized'))