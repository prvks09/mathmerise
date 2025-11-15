from app import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    icon = db.Column(db.String(50))
    topics = db.relationship('Topic', backref='category', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Topic(db.Model):
    __tablename__ = 'topic'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    difficulty = db.Column(db.String(20), default='beginner')  # beginner, intermediate, advanced
    views = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Topic {self.title}>'

class Formula(db.Model):
    __tablename__ = 'formula'
    
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    latex = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    topic = db.relationship('Topic', backref=db.backref('formulas', cascade='all, delete-orphan'))
    
    def __repr__(self):
        return f'<Formula {self.title}>'

class Example(db.Model):
    __tablename__ = 'example'
    
    id = db.Column(db.Integer, primary_key=True)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    problem = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    topic = db.relationship('Topic', backref=db.backref('examples', cascade='all, delete-orphan'))
    
    def __repr__(self):
        return f'<Example {self.title}>'
