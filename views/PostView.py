from flask.helpers import make_response


class PostView(object):
    def __init__(self):
        pass

    @classmethod
    def show(cls, post_id):
        return make_response("show post")
