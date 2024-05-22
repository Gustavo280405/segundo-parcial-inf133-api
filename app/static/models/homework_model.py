from database import db
from flask_login import UserMixin

class Homework(UserMixin, db.Model):
    __tablename__="tareas"
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    description=db.Column(db.String(128), nullable=False)
    status=db.Column(db.String(30), nullable=False)
    created_at=db.Column(db.String(128), nullable=False)
    assigned_to=db.Column(db.String(128), nullable=False)
    
    def __init__(self, id, title, description, status, crated_at, assigned_to):
        self.id=id
        self.title=title
        self.description=description
        self.status=status
        self.created_at=crated_at
        self.assigned_to=assigned_to
    
    def save(homework):
        db.session.add(homework)
        db.session.commit()
    
    def delete(homework):
        db.session.delete(homework)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Homework.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Homework.query.get(id)