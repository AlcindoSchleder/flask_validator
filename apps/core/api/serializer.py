from rules.configure_app import ma
from apps.core.model import Profiles
from flask_marshmallow.fields import fields


class ProfilesSerializer(ma.SQLAlchemyAutoSchema):
    id = fields.Str()
    doc_id = fields.Str(required=True)
    score = fields.Float(required=True)

    class Meta:
        model = Profiles
