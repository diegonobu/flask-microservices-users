class BaseConfig:
    DEBUG = False
    TESTING = False


class DevelopmentConfig:
    DEBUG = True


class TestingConfig:
    DEBUG = True
    TESTING = True


class ProductionConfig:
    DEBUG = False
