from datetime import datetime 
from . import db 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"Note('{self.title}', '{self.date_posted}')"
