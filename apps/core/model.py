from uuid import uuid4
from rules.configure_app import db


class Profiles(db.Model):
    id = db.Column(db.String(64), name='id', primary_key=True, default=str(uuid4()))
    doc_id = db.Column(db.String(80))
    score = db.Column(db.Float, default=1000.0)
