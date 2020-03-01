from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    calender = db.relationship('Calender', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Calender(db.Model):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    mon1 = db.Column(db.Boolean, default=False)
    mon2 = db.Column(db.Boolean, default=False)
    mon3 = db.Column(db.Boolean, default=False)
    mon4 = db.Column(db.Boolean, default=False)
    tues1 = db.Column(db.Boolean, default=False)
    tues2 = db.Column(db.Boolean, default=False)
    tues3 = db.Column(db.Boolean, default=False)
    tues4 = db.Column(db.Boolean, default=False)
    wed1 = db.Column(db.Boolean, default=False)
    wed2 = db.Column(db.Boolean, default=False)
    wed3 = db.Column(db.Boolean, default=False)
    wed4 = db.Column(db.Boolean, default=False)
    thurs1 = db.Column(db.Boolean, default=False)
    thurs2 = db.Column(db.Boolean, default=False)
    thurs3 = db.Column(db.Boolean, default=False)
    thurs4 = db.Column(db.Boolean, default=False)
    fri1 = db.Column(db.Boolean, default=False)
    fri2 = db.Column(db.Boolean, default=False)
    fri3 = db.Column(db.Boolean, default=False)
    fri4 = db.Column(db.Boolean, default=False)
    sat1 = db.Column(db.Boolean, default=False)
    sat2 = db.Column(db.Boolean, default=False)
    sat3 = db.Column(db.Boolean, default=False)
    sat4 = db.Column(db.Boolean, default=False)

    def get_all(self):
        return [self.id,\
        self.mon1, self.mon2, self.mon3, self.mon4, \
        self.tues1, self.tues2, self.tues3, self.tues4,\
        self.wed1, self.wed2, self.wed3, self.wed4,\
        self.thurs1, self.thurs2, self.thurs3, self.thurs4, \
        self.fri1, self.fri2, self.fri3, self.fri4, \
        self.sat1, self.sat2, self.sat3, self.sat4]
        

    def __repr__(self):
        return f"Calender('{self.id}','{self.date_posted}', \
        '{self.mon1}', '{self.mon2}', '{self.mon3}', '{self.mon4}', \
        '{self.tues1}', '{self.tues2}', '{self.tues3}', '{self.tues4}', \
        '{self.wed1}', '{self.wed2}', '{self.wed3}', '{self.wed4}', \
        '{self.thurs1}', '{self.thurs2}', '{self.thurs3}', '{self.thurs4}', \
        '{self.fri1}', '{self.fri2}', '{self.fri3}', '{self.fri4}', \
        '{self.sat1}', '{self.sat2}', '{self.sat3}', '{self.sat4}'"
 
class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon1 = db.Column(db.String(20), nullable=False, default='free')
    mon2 = db.Column(db.String(20), nullable=False, default='free')
    mon3 = db.Column(db.String(20), nullable=False, default='free')
    tues1 = db.Column(db.String(20), nullable=False, default='free')
    tues2 = db.Column(db.String(20), nullable=False, default='free')
    tues3 = db.Column(db.String(20), nullable=False, default='free')
    wed1 = db.Column(db.String(20), nullable=False, default='free')
    wed2 = db.Column(db.String(20), nullable=False, default='free')
    wed3 = db.Column(db.String(20), nullable=False, default='free')
    thurs1 = db.Column(db.String(20), nullable=False, default='free')
    thurs2 = db.Column(db.String(20), nullable=False, default='free')
    thurs3 = db.Column(db.String(20), nullable=False, default='free')
    fri1 = db.Column(db.String(20), nullable=False, default='free')
    fri2 = db.Column(db.String(20), nullable=False, default='free')
    fri3 = db.Column(db.String(20), nullable=False, default='free')
    sat1 = db.Column(db.String(20), nullable=False, default='free')
    sat2 = db.Column(db.String(20), nullable=False, default='free')
    sat3 = db.Column(db.String(20), nullable=False, default='free')

    def __repr__(self):
        return f"Shift('{self.id}', \
        '{self.mon1}', '{self.mon2}', '{self.mon3}', \
        '{self.tues1}', '{self.tues2}', '{self.tues3}', \
        '{self.wed1}', '{self.wed2}', '{self.wed3}', \
        '{self.thurs1}', '{self.thurs2}', '{self.thurs3}', \
        '{self.fri1}', '{self.fri2}', '{self.fri3}', \
        '{self.sat1}', '{self.sat2}', '{self.sat3}'"

                       
