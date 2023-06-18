
from flask import Flask, redirect, url_for
from flask_login import LoginManager, login_required

from .ot_user_manager import UserManager

import os

OTRoot = os.getcwd()

print('Initializing Old Times server...')
Old_Times_Version = 1
OTApp = Flask(__name__, static_url_path = '', static_folder=OTRoot + '/static_html', template_folder=OTRoot + '/templates')
OTApp.config['TEMPLATES_AUTO_RELOAD'] = True

OTApp.secret_key = 'secret key'
OTLoginManager = LoginManager()
OTLoginManager.init_app(OTApp)

@OTLoginManager.user_loader
def load_user(user_id):
    return UserManager.lookup_user(user_id)
print('hello')