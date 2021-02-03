# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def configure_database(app):
    db.init_app(app)
    app.db = db


def configure_serializers(app):
    ma.init_app(app)

class Config:
    """
        Class to define the type of environment configutation
        * class      Config, DevelopmentConfig, TestingConfig, ProductionConfig
        * requires   python 3.7
        * version    1.0.0
        * developer  Alcindo Schleder <alcindo.schleder@amcom.com.br>
    """

    SECRET_KEY = None
    HOST_SERVER = '0.0.0.0'
    SERVER_PORT = 5000
    DB_SERVER = '127.0.0.1'
    DATABASE_DRIVER = 'sqlite'
    DEBUG = False
    TESTING = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST_SERVER = '127.0.0.1'
    DATABASE_DRIVER = 'sqlite'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST_SERVER = '127.0.0.1'
    DB_SERVER = '127.0.0.1'
    DATABASE_DRIVER = 'sqlite'


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
