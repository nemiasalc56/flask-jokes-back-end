# jsonify lets us send JSON HTTP responses
from flask import Flask, jsonify, g
import models
# this is the main tool for coordinating the login/session
from flask_login import LoginManager

from resources.jokes import jokes
from resources.users import users






DEBUG = True # this prints helpful errors
PORT = 8000


app = Flask(__name__)

# set up a secret key
app.secret_key = "Secret keys are the best, only you know it."

# instantiate LoginManager to a login_manager
login_manager = LoginManager()

# connect the app with the login_manager
login_manager.init_app(app)

# using the blueprint to handle the horse stuff
app.register_blueprint(jokes, url_prefix='/api/v1/jokes')
app.register_blueprint(users, url_prefix='/api/v1/users')


# use this decorator to cause a function to run before request
@app.before_request
def before_request():
	# store the data as a global variable in g
	g.db = models.DATABASE
	g.db.connect()


# use this decorator to cause a function to run after request
@app.after_request
def after_request(response):
	g.db.close()
	return response


# create route to test the routes
@app.route('/')
def index():
	return "route is working"


# __name__ being '__main__' here means that we just ran this file
# as opposed to exporting i and importing it somewhere else
if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)