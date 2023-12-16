from datetime import datetime, timedelta

from flask import Flask

from lib.globals import register_jinja_globals
from services.index import register_index_endpoints


def initialize_app():
  app = Flask(__name__)

  register_jinja_globals(app)
  register_index_endpoints(app)

  return app

app = initialize_app()
