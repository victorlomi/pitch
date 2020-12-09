#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Comment, Pitch
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='bella')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_pitches(self):
        u1 = User(username='john')
        p = Pitch(body="example", author=u1)
        db.session.add(u1)
        db.session.add(p)
        db.session.commit()
        self.assertEqual(Pitch.query.filter_by(author=u1).first().body, p.body)

if __name__ == '__main__':
    unittest.main(verbosity=2)
