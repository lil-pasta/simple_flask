from flask import Blueprint

bp = Blueprint('functions', __name__)

from app.functions import routes
