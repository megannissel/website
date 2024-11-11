from urllib.parse import urlencode

from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user
from werkzeug.security import check_password_hash

from models.user import User
from services.sql import Session


def load_user(user_id):
  return Session.query(User).where(User.id==user_id).first()

def create_login_url(url):
  return "/login?%s" % urlencode([("return_page", url)])


def register_auth_endpoints(app):

  @app.route('/login')
  def login():
    return_page = request.args.get('next', '/recipes')
    return render_template('login.html',
      auth_flow=create_login_url(return_page)
    )


  @app.route('/login', methods=['POST'])
  def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = Session.query(User).where(User.username==username).first()

    if not user or not check_password_hash(user.password, password):
      flash('Please check your login details and try again.')
      return redirect(url_for('login'))

    login_user(user, remember=True)
    return_page = request.args.get('return_page', '/recipes')
    return redirect(return_page)
