from web import web
from flask import Flask

app = Flask(__name__)
app.register_blueprint(web)
