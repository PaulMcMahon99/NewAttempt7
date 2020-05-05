# Models hold the db tables used across the website.

from onlineshop import db,login_manager
from datetime import datetime
# Werkkzeug generates password hashing
from werkzeug.security import generate_password_hash,check_password_hash
# UserMixin enables correct password security.
# Example available at: https://github.com/lingthio/Flask-User/blob/master/flask_user/user_mixin.py
from flask_login import UserMixin

# This login manager decorator allows the website to track if a user is logged in
# via an if statement, allowing access to restricted view particular to each
# user, i.e. their reviews and their shopping cart. When it exists.

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    #this makes a table call users for each account to be associated with the
    # system.
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_image = db.Column(db.String(20), nullable=False, default='default_profile.png')
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # This connects BlogPosts to a User Author.
    posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
    # this password hashing is salted, so that it is immune to a
    # rainbow table attack. Each time the function is called,
    # the password hash is also different.
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"UserName: {self.username}"


# Development area start.

# Old 'Author' table Currently mothballed until tea works.
# class Supplier(db.Model):
#
#     __tablename__ = 'supplier'
#
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(20),nullable=False)
#     last_name = db.Column(db.String(30),nullable=False)
#     company_name = db.Column(db.String(30),nullable=False)
#     teas = db.relationship('Tea', backref='supplier', lazy=True)
#
#     def __repr__(self):
#         return f"Supplier('{self.first_name}', '{self.last_name}')"

# old 'Book' table
class Tea(db.Model):

    __tablename__ = 'tea'

    id = db.Column(db.Integer, primary_key=True)
    tea_name = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    tea_picture = db.Column(db.String(30), nullable=False, default='tea_default.png')
    stock_level = db.Column(db.Integer, nullable=False)
    supplier_name = db.Column(db.String(50), nullable=False)
    # Supplier as a foreign key is mothballed.
    # supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)

    def __repr__(self):
        return f"Tea('{self.tea_name}', '{self.description}', '{self.price}', '{self.stock_level}')"

# development area end.


class BlogPost(db.Model):
    # This initiates the review table and associates user to it.
    users = db.relationship(User)

    # This initiates the id for each review.
    id = db.Column(db.Integer, primary_key=True)
        # The foreign key with the review id creates a unique instance.
        # The date, title and text compose the review for the now, it does
        # not feature product information.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(140), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, title, text, user_id):
        self.title = title
        self.text = text
        self.user_id =user_id

    def __repr__(self):
        return f"Post Id: {self.id} --- Date: {self.date} --- Title: {self.title}"
