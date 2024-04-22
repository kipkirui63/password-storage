from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, UniqueConstraint, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

metadata = MetaData(naming_convention={
    "fk":"_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_Key=True)
    username = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(75), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable = False)


    passwords = db.relationship('User', back_populates='passwords')

    def __repr__(self):
        return f'(id={self.id}, username={self.username}, email={self.email})'
    
    def set_password(self,password):
        self.password_hash=generate_password_hash(password, method='scrypt:32768:8:1', salt_length=16)


    def check_password(self, password):
        return bcrypt.checkpw(self.password_hash.encode('utf-8'), password.encode('utf-8'))




class Password(db.Model):
    __tablename__ = 'passwords'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    website = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


    user = db.relationship('User', back_populates='passwords')

    def __repr__(self):
        return f'(website={self.website}, username={self.username}, password={self.password})'



