from dbs import mysql_db as db
from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, DateTime, TIMESTAMP, func, Boolean, DECIMAL
from uuid import uuid4
from flask_bcrypt import Bcrypt
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

bcrypt = Bcrypt()



roles_users = db.Table('roles_users',
        db.Column('user_id', db.String(36), db.ForeignKey('user.id')),
        db.Column('role_id', db.String(36), db.ForeignKey('role.id')))
class Role(db.Model, RoleMixin):
    #id = db.Column(db.String(36), primary_key=True)
    id = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()), comment='uuid', primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    
class User(db.Model, UserMixin):
    """Represents Proected users."""

    # Set the name for table
    #id = Column(db.Integer(), primary_key=True)
    id = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()), comment='uuid', primary_key=True)
    username = db.Column(db.String(255), unique=True)
    #password = db.Column(db.String(255))
    # current_login_at = Column(DateTime())
    create_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    # onupdate设置自动更改
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment='修改时间')
    login_count = Column(Integer)
    active = Column(Boolean(), default=True)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    
    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError('password not readable')
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8') 
        # or whatever other hashing function you like.

    '''
    def __init__(self, username, password):
        self.username = username
        self.password = self.set_password(password)
        self.active = True
        self.login_count = 0
    '''

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)
    
    def set_password(self, password):
        """Convert the password to cryptograph via flask-bcrypt"""
        return bcrypt.generate_password_hash(password).decode('utf-8') 
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)




    # flask-login 
    def is_authenticated(self):
        """Check the user whether logged in."""

        # Check the User's instance whether Class AnonymousUserMixin's instance.
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active():
        """Check the user whether pass the activation process."""

        return True

    def is_anonymous(self):
        """Check the user's login status whether is anonymous."""

        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        """Get the user's uuid from database."""

        return self.id








