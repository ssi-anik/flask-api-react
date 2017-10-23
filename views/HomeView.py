from flask.helpers import make_response


class HomeView(object):
    def __init__(self):
        pass

    @classmethod
    def index(cls):
        return make_response("HomeView@index"), 200
