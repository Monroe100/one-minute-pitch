from . import main

@main.route('/')
def index():
    return '<h1> pitches </h1>'

