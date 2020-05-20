import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# Note: you may need to initiate this from the command line at some future point:
# source activate myflask
# export SECRET_KEY=mysecret
# set SECRET_KEY=mysecret

# This is the setup of the main database.
# The line below lifts the location where the main project source code lies
app.config['SECRET_KEY'] = 'mysecret'


# This is the setup of the main database.
# The line below lifts the location where the main project source code lies
basedir = os.path.abspath(os.path.dirname(__file__))
# this is the location being used to place the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# This setting prevents the DB from tracking modifications, which is not needed here.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#  this passes the app to the db, and migrate makes the
# live connection between the two.
db = SQLAlchemy(app)
Migrate(app,db)


# this collects the log in manager for configuration
login_manager = LoginManager()

# the login manager is now passed the app
login_manager.init_app(app)

# This will move the users to the login screen when called
login_manager.login_view = "users.login"

# To make this function, the non-functioning pages have been commented out.
# This is the shop and the cart.

# The bluerints used in the project are controlled here, they
# are registered to the app by this configuration.
from onlineshop.core.views import core
from onlineshop.users.views import users
from onlineshop.blog_posts.views import blog_posts
from onlineshop.error_pages.handlers import error_pages
# from onlineshop.shop.views import shop_items

# here are the blueprints so far.
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
# app.register_blueprint(shop_items)
