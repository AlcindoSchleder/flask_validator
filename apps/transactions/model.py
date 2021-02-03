from uuid import uuid4
from datetime import datetime
from rules.configure_app import db


class Transactions(db.Model):
    id = db.Column(db.String(64), name='id', primary_key=True, default=uuid4)
    customer_id = db.Column(
        db.Integer, db.ForeignKey('Profiles.id'), nullable=False
    )
    score = db.Column(db.Float, default=1000.0)
    income = db.Column(db.Float, default=0.0)
    requested_value = db.Column(db.Float, default=0.0)
    installments = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    time = db.Column(db.DateTime, default=datetime.now)
