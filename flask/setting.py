from distutils.debug import DEBUG
from os import urandom

DEBUG = True
SECRET_KEY = urandom(24)
