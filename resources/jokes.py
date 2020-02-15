import models

from flask import Blueprint



# the first arg is the blueprint's name
# and the second arg is its import_name
jokes = Blueprint('jokes', 'jokes')



jokes.route('/')
def jokes_index():

	return "jokes resource is working!"
