class Configuration(object):
    SECRET_KEY = 'qwerty'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://kompl@localhost/testdbflask'

    ###Flask Security###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
