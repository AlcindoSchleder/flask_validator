from uuid import uuid4
from rules.configure_app import db
from sqlalchemy import UniqueConstraint


class Profiles(db.Model):
    id = db.Column(
        db.Integer, name='id', primary_key=True,
        default=0, sqlite_autoincrement=True
    )
    uuid = db.Column(
        db.String(64), name='uuid', default=str(uuid4())
    )
    doc_id = db.Column(db.String(80))
    score = db.Column(db.Float, default=1000.0)
    revenue = db.Column(db.Float, default=0.0)
    UniqueConstraint('uuid', name='profiles_uuid_idx')
    UniqueConstraint('doc_id', name='profiles_document_idx')
