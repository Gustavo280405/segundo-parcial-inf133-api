from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

class User(UserMixin,db.Model):
    __tablename__="Usuarios"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(128), nullable=False)
    password=db.Column(db.String(128), nullable=False)
    role=db.Column(db.String(15), nullable=False, default="user")
    
    def __init__(self, id, name, email, password, role="user"):
        self.id=id
        self.name=name
        self.email=email
        self.Pon_password=password
        self.role=role
    
    def Pon_password(password):
        password=generate_password_hash
    
    def save(user):
        db.session.add(user)
        db.session.commit()
    
    def delete(user):
        db.session.delete(user)
        db.session.commit()
    
    
    @staticmethod
    def get_all():
        return User.query.all()
    
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    def has_Role(self, Role):
        return self.Role==Role