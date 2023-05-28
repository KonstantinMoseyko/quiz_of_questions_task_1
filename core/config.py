import os
from dotenv import load_dotenv


load_dotenv()


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
   
    
class DevConfig(BaseConfig):
    DEBUG = True
    
    
class TestingConfig(BaseConfig):
    TESTING = True
    