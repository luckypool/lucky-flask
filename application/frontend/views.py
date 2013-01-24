from flask import Module, render_template

frontend = Module(__name__, "frontend")

@frontend.route("/")
def index():
    asign_params = {
        'page_title' : 'frontend.index',
        'one' : 'hello',
        'two' : 'world'
    }
    print asign_params
    return render_template('frontend/index.html', **asign_params)

