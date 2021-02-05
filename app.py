#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask_migrate import Migrate
from rules.configure_app import configure_database, configure_serializers, config_by_name


def load_environment():
    if os.path.exists('.env'):
        with open('.env') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                key, value = line.strip().split('=', 1)
                os.environ[key] = value   # Load to local environ


def configure_app(app):
    load_environment()
    app.config.FLASK_ENV = os.environ.get("FLASK_ENV", default="development")
    database_name = os.environ.get("DATABASE_NAME", default="data.db")
    mode = config_by_name[app.config.FLASK_ENV]
    # Configure SQLAlchemy set to relative path
    app.config['SQLALCHEMY_DATABASE_URI'] = f'{mode.DATABASE_DRIVER}:///data/data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = mode.SQLALCHEMY_TRACK_MODIFICATIONS


def create_app():
    """
    Configure Flask and Database
    :return: FlaskObject
    """
    app = Flask(__name__)   # Configure App

    configure_app(app)              # Get config from .env file
    configure_database(app)         # Configure database
    configure_serializers(app)      # Configure Marshmallow Serializers

    Migrate(app, app.db)    # Create and Migrate Database

    from apps.core.routes import bp_profile
    from apps.transactions.routes import bp_transaction
    app.register_blueprint(bp_profile)          # Register blueprint route from Profiles
    app.register_blueprint(bp_transaction)      # Register blueprint route from Transactions

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
