#coding:utf-8
from extensions import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.String(5000),nullable=False)
    url_add = db.Column(db.String(500), nullable=False)
    date_tweeter = db.Column(db.String(100), nullable=False)
    tf_idf = db.Column(db.String(100),nullable=False)
    key_words = db.Column(db.String(100), nullable=False)
    # new_feature1 = db.Column(db.Integer,nullable=True)
    #foreignKey link with table 'user'
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    #relation link with Class 'User'
    user = db.relationship('User',backref=db.backref('articles'))

class Readability(db.Model):
    __tablename__ = 'readability'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    # foreignKey link with table 'user'
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    url_add = db.Column(db.String(500),nullable=False)
    readability_rate = db.Column(db.Integer,nullable=False)
    # relation link with Class 'User'
    user = db.relationship('User',backref=db.backref('readability'))

