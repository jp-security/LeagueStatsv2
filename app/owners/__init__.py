from flask import Blueprint

owners = Blueprint('owners', __name__)

from . import routes
