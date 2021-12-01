import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    SECRET = os.environ.get("SECRET")
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER")


class DevelopmentConfig:
    DEBUG = True


class TestingConfig:
    TESTING = True
    DEBUG = True


class ProductionConfig:
    DEBUG = False
    TESTING = False
