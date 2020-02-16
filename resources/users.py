import models
from flask import Blueprint, request


# make this a blueprint
users = Blueprint('users', 'users')


@users.route('/', methods=['GET'])
def test():
	return "we have a user resource"



# register route (create 'POST')
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	print(payload)

	return "register route works"