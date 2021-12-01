import logging
from flask import Flask

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)

if app.config.get("ENV") == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config.get("ENV") == "testing":
    app.config.from_object("config.TestingConfig")
elif app.config.get("ENV") == "development":
    app.config.from_object("config.DevelopmentConfig")

from app.mod.views import blueprint_abod

app.register_blueprint(blueprint_abod, url_prefix="/")