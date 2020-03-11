from flask import Blueprint

from ..models import Engine

home = Blueprint(
    'home',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/home-static'
)

from . import views
