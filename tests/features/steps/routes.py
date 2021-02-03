# -*- coding: utf-8 -*-
"""
    Unit        : tests.features.steps
    description : Define the steps of test of routes from flask
    developer   : Alcindo Schleder
    version     : 1.0.0
"""
import json
from behave import given, when, then
from requests import post


"""
    Cenário: Um Json Inválido
"""
@given('Um json inválido')
def receive_invalid_json(context):
    context.data = context.text


@when('Enviar o json inválido')
def send_invalid_json(context):
    context.api_request = post(
        context.base_url,
        json=json.loads(context.data)
    )


@then("Api deve retornar {status_code:d} inválido")
def chek_invalid_status_code(context, status_code):
    assert context.api_request.status_code == status_code


"""
    Cenário: Um Json Válido
"""
@given('Um json Válido')
def get_valid_json(context):
    context.data = context.text

@when('Enviar o json válido')
def send_valid_json(context):
    context.api_request = post(
        context.base_url,
        json=json.loads(context.data)
    )


@then("Api deve retornar {status_code:d} válido")
def chek_valid_status_code(context, status_code):
    assert context.api_request.status_code == status_code
