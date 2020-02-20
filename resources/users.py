import models
from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user


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
		models.User.get(models.User.username == payload['username'])
		# if the query doesn't cause an error, then the user exists
		print(payload['username'])

		return jsonify(
			data={},
			message="A user with that username already exists",
			status=401
			), 401

	# if we get the error, the user does not exist
	# so can proceed
	except models.DoesNotExist:
		# create user
		new_user = models.User.create(
			first_name=payload['first_name'],
			last_name=payload['last_name'],
			username=payload['username'],
			password=generate_password_hash(payload['password']),
			email=payload['email']
			)
		print("it is getting here")

		# this logs in the user and starts a session
		login_user(new_user)

		# convert the data to a dictionary
		user_dict = model_to_dict(new_user)
		print(user_dict['password'])

		# we can't jsonify the password (generated_password_hash)
		# and we don't need to send it, so we can remove it
		user_dict.pop('password')

		# return "user was created"
		return jsonify(
			data=user_dict,
			message="Successfully created a user",
			status=201
			), 201


@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	print(payload)


	try:
		#look user up by username
		user = models.User.get(models.User.username == payload['username'])
		print(user)

		# if that didn't cuase an error, let's check the password
		user_dict = model_to_dict(user)

		# check the password
		passwor_is_good = check_password_hash(user_dict['password'], payload['password'])

		if passwor_is_good:
			# log the user in the app using flask
			login_user(user)
			user_dict.pop('password')

			return jsonify(
				data=user_dict,
				message=f"Successfully looged in {user_dict['first_name']} {user_dict['last_name']}",
				status=200
				), 200
		else:
			print("password no good")

			return jsonify(
				data={},
				message="Username or password is incorrect.",
				status=401
				), 401



	except models.DoesNotExist:

		return jsonify(
			data={},
			message="Username or password is incorrect."
			)


# route to show the user that is logged in
@users.route('/logged_in', methods=['GET'])
def logged_in():
	print(current_user)
	print(type(current_user))


	if not current_user.is_authenticated:
		return jsonify(
		data={},
		message="No user is currently logged in.",
		status=401
		), 401
	else:
		user_dict = model_to_dict(current_user)
		user_dict.pop('password')

		return jsonify(
			data=user_dict,
			message="Found logged in user",
			status=200
		), 200



# logout route
@users.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
		data={},
		message="The user was successfully logged out.",
		status=201
		), 201

# update route
@users.route('/<id>', methods=['PUT'])
def edit_user(id):
	# get the info from the request
	payload = request.get_json()
	print(payload)

	# find the user
	user = models.User.get_by_id(id)
	print(user)

	# update the info
	user.first_name = payload['first_name']
	user.last_name = payload['last_name']
	user.password = payload['password']
	user.email = payload['email']

	# convert model to dictionary
	user_dict = model_to_dict(user)
	return jsonify(
		data=user_dict,
		message=f"Successfully update user.",
		status=200
		), 200


# destroy route
@users.route('/<id>', methods=['Delete'])
def delete_user(id):
	# find the user
	user = models.User.get_by_id(id)
	print(user)
	# delete user
	user.delete_instance()

	return jsonify(
		data={},
		message="Successfully delete user account.",
		status=200
		), 200

