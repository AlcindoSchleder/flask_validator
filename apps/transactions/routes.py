from flask import Blueprint, current_app, request
from marshmallow import ValidationError
from .model import Transactions
from .api.serializer import TransactionsSerializer
from sqlalchemy import desc

bp_transaction = Blueprint('transaction', __name__, url_prefix='/transaction')

@bp_transaction.route('/list', methods=['GET'])
def list():
    bs = TransactionsSerializer(many=True)
    res = Transactions.query.all()
    return bs.jsonify(res), 200

@bp_transaction.route('/show/<id>', methods=['GET'])
def show(id: str):
    bs = TransactionsSerializer()
    try:
        res = Transactions.query.filter_by(id=id).first()
        if res == {}:
            res = {'message': f'User with id "{id}" returns a empty query!'}
    except Exception as e:
        return {"message": f"Error on read Database:\n    {e}\n    data: {res}"}
    return bs.jsonify(res), 200


@bp_transaction.route('/customer_last/<int:id>', methods=['GET'])
def customer_last(id: str):
    bs = TransactionsSerializer()
    try:
        res = Transactions.query.filter_by(customer_id=id)\
            .order_by(desc(Transactions.time)).first()
    except Exception as e:
        return {"message": f"Error on read Database:\n    {e}\n    data: {res}"}
    return bs.jsonify(res), 200


@bp_transaction.route('/delete/<id>', methods=['DELETE'])
def delete(id: str):
    bs = TransactionsSerializer()
    try:
        Transactions.query.filter(Transactions.id == id).delete()
        current_app.db.session.commit()
        res = {'message': f'Register of profile id: {id} deleted successfully!'}
    except Exception as e:
        res = {
            "message": f"Profile not Found. "
                       f"Not update data with error:"
                       f"\n    {e}"
                       f"\n    data: {id}"
            }, 404
    return bs.jsonify(res), 200


@bp_transaction.route('/update/<id>', methods=['PUT'])
def update(id: str):
    bs = TransactionsSerializer()
    try:
        query = Transactions.query.filter(Transactions.id == id)
        query.update(request.json)
        current_app.db.session.commit()
        res = Transactions.first()
    except Exception as e:
        res = {
            "message": f"Profile not Found. "
                       f"Not update data with error:"
                       f"\n    {e}"
                       f"\n    data: {request.json}"
            }, 404
    return bs.jsonify(res), 200


@bp_transaction.route('/insert', methods=['POST'])
def insert():
    bs = TransactionsSerializer()
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        res = Transactions(**bs.load(json_data))
    except ValidationError as err:
        return err.messages, 422
    try:
        # current_app.db.session.add(profile)
        current_app.db.session.add(res)
        current_app.db.session.commit()
    except Exception as e:
        res = {"message": f"Not insert data with error:\n    {e}\n    data: {profile}"}
    return bs.jsonify(res), 201
