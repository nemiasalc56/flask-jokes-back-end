import models
from flask import Blueprint


# make this a blueprint
users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def test():
	return "we have a user resource"