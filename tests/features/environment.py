# -*- coding: utf-8 -*-
"""
    Unit        : tests.environment
    Description : Define environment configuration to execute the tests
    developer   : Alcindo Schleder
    version     : 1.0.0
"""
import os
import sys
import ipdb
from rules.start import InitializeProgram
# from common import COMMON_DIRECTORY
# from server import server_app
# from workspaces.home.view import HomeRoute

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

# CONFIGURE_FILE = f'{COMMON_DIRECTORY}/config.json'
# CONFIGURE_HASH = os.environ.get(
#     "CONFIG_HASH",
#     default="b17913cc95df7a21eb8faa3fb55571e70f963f26a613bc72677842033506f32c"
# )
# CONFIGURE_DATA = "COMPANY_SECURITY_DATA"


def before_all(context):
    context.base_url = context.config.userdata


def before_feature(context, feature):
    context.root_path = os.path.dirname(os.path.dirname(ROOT_PATH))
    context.data_path = f'{ROOT_PATH}/data'
    context.app = InitializeProgram(True)

    # context.flask = server_app
    # context.flask.testing = True
    # context.flask_context = context.flask.test_request_context()
    # context.flask_context.push()
    # context.client = context.flask.test_client()


def after_feature(context, feature):
    """
    Actions after testing each feature
    @param context: Context of feature
    @param feature: Current feature
    @return: void
    """


def after_step(context, step):
    """
    Actions to execute on each step of test
    @param context: step context
    @param step: current step
    @return: void
    """
    if step.status == 'failed':
        ipdb.spost_mortem(step.exc_traceback)
