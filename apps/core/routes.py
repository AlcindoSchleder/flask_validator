from flask import Blueprint, current_app, request
from marshmallow import ValidationError
from .model import Profiles
from .api.serializer import ProfilesSerializer

bp_profile = Blueprint('profile', __name__, url_prefix='/profile')

@bp_profile.route('/list', methods=['GET'])
def list():
    ps = ProfilesSerializer(many=True)
    res = Profiles.query.all()
    return ps.jsonify(res), 200

@bp_profile.route('/show/<id>', methods=['GET'])
def show(id: str):
    ps = ProfilesSerializer()
    try:
        res = Profiles.query.filter_by(id=id).first()
        if res == {}:
            res = {'message': f'User with id "{id}" returns a empty query!'}
    except Exception as e:
        return {"message": f"Error on read Database:\n    {e}\n    data: {res}"}
    return ps.jsonify(res), 200

@bp_profile.route('/delete/<id>', methods=['DELETE'])
def delete(id: str):
    ps = ProfilesSerializer()
    try:
        Profiles.query.filter(Profiles.id == id).delete()
        current_app.db.session.commit()
        res = {'message': f'Register of profile id: {id} deleted successfully!'}
    except Exception as e:
        res = {
            "message": f"Profile not Found. "
                       f"Not update data with error:"
                       f"\n    {e}"
                       f"\n    data: {id}"
            }, 404
    return ps.jsonify(res), 200


@bp_profile.route('/update/<id>', methods=['PUT'])
def update(id: str):
    ps = ProfilesSerializer()
    try:
        query = Profiles.query.filter(Profiles.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        res = Profiles.first()
    except Exception as e:
        res = {
            "message": f"Profile not Found. "
                       f"Not update data with error:"
                       f"\n    {e}"
                       f"\n    data: {request.json}"
            }, 404
    return ps.jsonify(res), 200


@bp_profile.route('/insert', methods=['POST'])
def insert():
    ps = ProfilesSerializer()
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        profile = Profiles(**ps.load(json_data))
    except ValidationError as err:
        return err.messages, 422
    try:
        # current_app.db.session.add(profile)
        current_app.db.session.add(profile)
        current_app.db.session.commit()
    except Exception as e:
        return {"message": f"Not insert data with error:\n    {e}\n    data: {profile}"}
    return ps.jsonify(profile), 201
