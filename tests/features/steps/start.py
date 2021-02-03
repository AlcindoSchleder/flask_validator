# -*- coding: utf-8 -*-
"""
    Unit        : tests.features.steps
    description : Define the steps of test
    developer   : Alcindo Schleder
    version     : 1.0.0
"""
import os
from argparse import Namespace
from behave import given, when, then


@given('Aplicação é iniciada para o arquivo {fn}')
def instance_initial_application_class(context, fn):
    context.filename = f'{context.data_path}/{fn}'


@when('Configura a classe InitializeProgram._parser')
def prepare_app(context):
    context.parser = context.app._configure_parser()
    if context.parser is not None:
        context.parser.parse_args(['--input', context.filename])
        context.app._parser = context.parser
        context.app._args = Namespace(input=context.filename)
        context.app.testing = True


@then("Verifica se existe o arquivo")
def check_file_exists(context):
    assert os.path.exists(context.filename)


@then('Inicia o processamento das Transaçoes do arquivo')
def start_file_processing(context):
    assert context.app.start()
