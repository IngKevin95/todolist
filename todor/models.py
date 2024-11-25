#from flask_sqlalchemy import SQLAlchemy
from todor import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    state = db.Column(db.Boolean, default=False)

    def __init__(self,created_by,title,description,state=False):
        self.created_by = created_by
        self.title = title
        self.description = description
        self.state = state

    def __repr__(self):
        return f'<ToDo: {self.title}>'