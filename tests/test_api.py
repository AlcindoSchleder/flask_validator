from unittest import TestCase
from flask import Flask
import app


class TestFlaskAPI(TestCase):
    def test_create_app_must_exixts(self):
        self.assertEqual(
            hasattr(app, 'create_app'),
            True,
            'App Factory not exists'
        )

    def test_create_app_must_callable(self):
        self.assertEqual(
            hasattr(app.create_app, '__call__'),
            True,
            'Create App must be callable'
        )

    def test_create_app_must_return_app(self):
        self.assertIsInstance(
            app.create_app(),
            Flask,
            'Create App must be a Instace of Flask APP'
        )

