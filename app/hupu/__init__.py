from flask import Blueprint

hupu = Blueprint('hupu', __name__)

from . import   views
