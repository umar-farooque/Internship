from flask import Blueprint

from ..models import Engine

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views
