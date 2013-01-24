from flask import Flask
from application.frontend.views import frontend
from application.jsonrpc.views import jsonrpc

__version__ = 0.1

app = Flask(__name__)
app.config.from_object("application.config.DevelopConfig")

app.register_module(frontend, url_prefix="/")
app.register_module(jsonrpc, url_prefix="/jsonrpc")

