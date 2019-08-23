class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:sec123@127.0.0.1:5432/EMS'
    SECRET_KEY = 'some'


class ProductionConfig(Config):
    DEBUG = False
