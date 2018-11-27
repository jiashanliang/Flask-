from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    u_name = db.Column(db.String(64),unique=True)
    u_password = db.Column(db.String(256))
    u_email = db.Column(db.String(128))
    u_active = db.Column(db.Boolean,default=False)
    u_icon = db.Column(db.String(128))
    is_delete=db.Column(db.Boolean,default=False)

class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    b_title = db.Column(db.String(128),unique=True)
    b_content = db.Column(db.Text())
    #当博客被删除后，状态变为False
    b_active = db.Column(db.Boolean,default=True)

class Collection(db.Model):
    c_id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    u_id = db.Column(db.Integer, db.ForeignKey(User.id),unique=True)
    b_id = db.Column(db.Integer, db.ForeignKey(Blog.id))