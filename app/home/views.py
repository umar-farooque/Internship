from . import home

@home.route('/')
def index():
    return "Home Page Of Internship"