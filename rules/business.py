# -*- coding: utf8 -*-
import json
from datetime import datetime
from requests import get, post
from apps.transactions.api.serializer import TransactionsSerializer

class BusinessValidation:
    """
    Class to validate transactions as the rules defined by customer
    """
    _HOST = 'localhost:5000/'
    _transaction = None
    _ts = None
    valid_msg = []

    def __init__(self, transaction):
        self._ts = TransactionsSerializer()

    def _valitate_json(self):
        try:
            if type(self.transaction) == str:
                self.transaction = json.loads(self.transaction)
            self._ts.load(self.transaction)
        except Exception as e:
            print(f'Error on load transaction. This is not a valid json '
                   f'trasaction.\n Error: {e}')
            return False

    def _get_customer_data(self, id):
        try:
            data = get(f'{self._HOST}/profile/show/{id}')
            if data.status_code != 200:
                self.valid_msg.append(f'Error on reading customer data, '
                                      f'code status {data.status_code}!')
                return False
            return data.json()
        except Exception as e:
            self.valid_msg.append(f'Error on reading customer data!\n Error: {e}')
            return {}

    def _get_last_transaction_data(self, id):
        try:
            data = get(f'{self._HOST}/transactions/customer_last/{id}')
            if data.status_code != 200:
                self.valid_msg.append(f'Error on reading customer data, '
                                      f'code status {data.status_code}!')
                return False
        except Exception as e:
            self.valid_msg.append(f'Error on reading customer data!\n Error: {e}')
            return {}
        return data.json()

    def _rule_revenue(self):
        res = True
        MAX_COMMITMENT = 30
        installments_value = self._ts.requested_value / self._ts.installments
        income_commitment = (self._ts.income * (MAX_COMMITMENT / 100))
        if installments_value > income_commitment:
            self.valid_msg.append(f'Installments is greater then 30% of customers revenue! ')
            res = False
        return res

    def _rule_score(self):
        MIN_SCORE = 200
        if self._ts.score < MIN_SCORE:
            self.valid_msg.append(f'Score of customer not approved!')
            res = False

    def _last_transaction(self):
        MIN_REQUEST_TIME = 2
        res = True
        data = self._get_last_transaction_data(self._ts.customer_id)
        if data != {}:
            last_time = datetime.strptime(data['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
            current_time = datetime.now()
            actual_time = current_time - last_time
            if (actual_time.seconds / 60) <= MIN_REQUEST_TIME:
                self.valid_msg.append(f'New Transaction must has a interval'
                                      f' greather then {MIN_REQUEST_TIME}')
                res = False
        return res

    def validate(self, data):
        self._transaction = data
        if self._valitate_json():
            self._rule_revenue()
            self._rule_score()
            self._last_transaction()
            if self.valid_msg == []:
                post(f'{self._HOST}/transactions/insert', data=self._transaction)
        return self.valid_msg
