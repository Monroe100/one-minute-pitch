import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
 
class ProdConfig(Config):
    pass


class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}