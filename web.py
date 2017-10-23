from flask import Flask
from flask.blueprints import Blueprint

from views.HomeView import HomeView
from views.PostView import PostView

web = Blueprint('web', __name__)
DEBUG = True


@web.route('/')
def index():
    return HomeView().index()


@web.route('/posts/<int:post_id>', methods=['GET'])
def show_post(post_id):
    return PostView().show(post_id)
