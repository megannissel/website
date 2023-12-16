from datetime import datetime

def register_jinja_globals(app):

  app.jinja_env.globals.update(
    CURRENT_YEAR = datetime.today().strftime("%Y"),
  )
