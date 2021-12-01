import os
from uuid import uuid1
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

blueprint_abod = Blueprint("abod", __name__, template_folder="templates", static_folder="static", static_url_path="/static")

# UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {"pdf"}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint_abod.route("/", methods=["GET"])
def index():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        return abort(404)


@blueprint_abod.route("/result", methods=["GET"])
def result():
    try:
        return render_template("result.html")
    except TemplateNotFound:
        return abort(404)