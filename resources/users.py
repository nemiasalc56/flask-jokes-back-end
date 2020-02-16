import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash


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

	# make username and email lowercase
	payload['username'] = payload['username'].lower()
	payload['email'] = payload['email'].lower()

	try:
		# check if the user already exists
		# if they do, we won't create the user
		models.User.get(models.User.email == payload['email'])
		# if the query doesn't cause an error, then the user exists
		print(payload['email'])

		return jsonify(
			data={},
			message="A user with that email already exists",
			status=401
			), 401

	# if we get the error, the user does not exist
	# so can proceed
	except models.DoesNotExist:
		

		return "user does not exist"