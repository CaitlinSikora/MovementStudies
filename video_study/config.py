# -*- coding: utf-8 -*-
__author__ = 'seb'
import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SQLALCHEMY_ECHO = True
SECRET_KEY = "the SECRET"
WTF_CSRF_ENABLED = True
# Disable debugging
DEBUG = True