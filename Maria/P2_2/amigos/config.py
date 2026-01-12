class Config:
    """Clase base"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Desarrollo"""
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Producción"""
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}