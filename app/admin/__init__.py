from flask import Blueprint

# from ..models import Engine

admin = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from . import views
from .manage.users import *
from .manage.courses import *