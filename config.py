import os

class Config:
    SQLALCHEMY_DATABASE_URI = ('DATABASE_URI', 'postgresql+psycopg2://michelle:kajuju@localhost/pitches')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
}