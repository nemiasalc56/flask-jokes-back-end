# jsonify lets us send JSON HTTP responses
from flask import Flask
import models
from resources.jokes import jokes




DEBUG = True # this prints helpful errors
PORT = 8000


app = Flask(__name__)


# using the blueprint to handle the horse stuff
app.register_blueprint(jokes, url_prefix='/api/v1/jokes')


# create route to test the routes
@app.route('/')
def index():
	return "route is working"


# __name__ being '__main__' here means that we just ran this file
# as opposed to exporting i and importing it somewhere else
if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)