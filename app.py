# jsonify lets us send JSON HTTP responses
from flask import Flask, jsonify, g
import models
from resources.jokes import jokes

# this is the main tool for coordinating the login/session
from flask_login import LoginManager





DEBUG = True # this prints helpful errors
PORT = 8000


app = Flask(__name__)

# set up a secret key
app.secret_key = "Secret keys are the best, only you know it."

# instantiate LoginManager to a login_manager
login_manager = LoginManager()


# using the blueprint to handle the horse stuff
app.register_blueprint(jokes, url_prefix='/api/v1/jokes')



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