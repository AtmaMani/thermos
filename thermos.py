from flask import Flask
app = Flask(import_name=__name__)
import json
from executor import generate_unique_random_integers
from flask import request

@app.route('/')
def hello_world():
    return_dict = {'level':'/',
                   'message':'Hello user!'}

    return json.dumps(return_dict)

@app.route('/user/<string:username>')
def show_user_profile(username):
    if username == 'atma':
        user_id = 1
    elif username == 'su':
        user_id = 2
    else:
        user_id = 99

    return_dict = {'level':'/user/{}'.format(username),
                   'user_id':user_id}

    return json.dumps(return_dict)

@app.route('/genrandom')
def generate_random_ints():
    """
    Called as 127.0.0.1:5000/genrandom?numRandom=20&upperLimit=30
    :return:
    """
    query = request.args.to_dict()

    num_random = int(query['numRandom']) if 'numRandom' in query else None
    upper_limit = int(query['upperLimit']) if 'upperLimit' in query else None

    random_list = generate_unique_random_integers(num_random, upper_limit)

    return json.dumps(random_list)