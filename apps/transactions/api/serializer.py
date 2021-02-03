from datetime import datetime
from rules.configure_app import ma
from apps.transactions.model import Transactions
from flask_marshmallow.fields import fields


class TransactionsSerializer(ma.SQLAlchemyAutoSchema):
    id = fields.Str()
    customer_id = fields.Str(required=True)
    doc_id = fields.Str(required=True)
    score = fields.Float(required=True, default=0.0)
    income = fields.Float(required=True, default=0.0)
    requested_value = fields.Float(required=True, default=0.0)
    installments = fields.Integer(required=True, default=0)
    status = fields.Integer(required=True, default=400)
    time = fields.DateTime(requested=True, default=datetime.now)

    class Meta:
        model = Transactions
        include_fk = True
