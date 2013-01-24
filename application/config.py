class Config(object):
    DEBUG = False
    TESTING = False
    ROOT = '0.0.0.0'

class ProductConfig(Config):
    pass

class DevelopConfig(Config):
    DEBUG = True
