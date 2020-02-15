# jsonify lets us send JSON HTTP responses
from flask import Flask




DEBUG = True # this prints helpful errors
PORT = 8000


app = Flask(__name__)



# __name__ being '__main__' here means that we just ran this file
# as opposed to exporting i and importing it somewhere else
if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)