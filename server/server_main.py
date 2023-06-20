
from flask import Flask, redirect, url_for, render_template, flash, request
from flask_login import LoginManager, login_required

import flask_login

from .ot_user_manager import UserManager
from .ot_user import OTUser
from .ot_scenario import OTScenario

import os
import sys

OTRoot = os.getcwd()

print('Initializing Old Times server...')
Old_Times_Version = 1
OTApp = Flask(__name__, static_url_path = '', static_folder=OTRoot + '/static_html', template_folder=OTRoot + '/templates')
OTApp.config['TEMPLATES_AUTO_RELOAD'] = True

OTApp.secret_key = 'secret key'
OTLoginManager = LoginManager()
OTLoginManager.init_app(OTApp)

OTUserManager = UserManager()

@OTLoginManager.user_loader
def load_user(user_id):
    return OTUserManager.lookup_user(user_id)

@OTApp.route('/')
@flask_login.login_required
def get_home_page():
  flash('Welcome ' + flask_login.current_user.name + '!  Prepare to die!')
  return render_template('start_page.html', version = Old_Times_Version)

@OTApp.route('/begin_game')
@flask_login.login_required
def begin_game():
  user : OTUser = flask_login.current_user

  if user.scenario == None:
    print('Need to start a scenario!')
    user.set_scenario(OTScenario('First Scenario'))
  else:
    print('Scenario already established')
  sys.stdout.flush()
  return render_template('begin_game.html', name = user.name, scenario = user.scenario)

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

@OTLoginManager.unauthorized_handler
def unauthorized_handler():
  print('login unauthorized!')
  return redirect(url_for('get_authorized'))