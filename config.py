
<<<<<<< HEAD

=======
>>>>>>> c74fb1c5c010f7302e5447fd11140ed96877d666
import os

class Config:
    '''
    General configuration parent class
    '''


    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


<<<<<<< HEAD
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kajuju@localhost/pitch'


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
=======


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:michelle@localhost/oneminutepitch'


   
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
>>>>>>> c74fb1c5c010f7302e5447fd11140ed96877d666
