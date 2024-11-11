import os
from datetime import datetime, timedelta

from flask import Flask
from flask_login import LoginManager

from lib.globals import register_jinja_globals
from services.auth import register_auth_endpoints, load_user
from services.index import register_index_endpoints
from services.recipes import register_recipe_endpoints
from services.sql import Session


def initialize_app():
  app = Flask(__name__)

  app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

  register_jinja_globals(app)
  register_auth_endpoints(app)
  register_index_endpoints(app)
  register_recipe_endpoints(app)

  login_manager = LoginManager()
  login_manager.login_view = "login"
  login_manager.user_loader(load_user)
  login_manager.init_app(app)

  return app

app = initialize_app()

@app.teardown_appcontext
def cleanup(resp_or_exc):
  Session.remove()
