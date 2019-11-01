# basic imports
from flask import Flask
app = Flask(import_name=__name__)

# import to parse wildcard args
from flask import request

# import to render html pages
from flask import render_template

# other imports
import json
from executor import generate_unique_random_integers
import os, sys, socket

# define the root resource
@app.route('/', methods=['GET'])
def index_page():

    return render_template('index.html',
                           sys_path = str(sys.path),
                           os_type = str(sys.platform),
                           os_name = str(os.name),
                           mac_name = str(socket.gethostname()),
                           mac_ip = str(socket.gethostbyname(socket.gethostname())))

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    Called as /hello?name='atma'
    :return:
    """
    # if user sends payload to variable name, get it. Else empty string
    name = request.args.get('name', '')
    return f'Hello {name}'


@app.route('/genUniqueRandom', methods=['GET'])
def generate_random_ints():
    """
    Called as 127.0.0.1:5000/genUniqueRandom?numRandom=20&upperLimit=30
    :return:
    """
    query = request.args.to_dict()

    num_random = int(query['numRandom']) if 'numRandom' in query else None
    upper_limit = int(query['upperLimit']) if 'upperLimit' in query else None

    random_list = generate_unique_random_integers(num_random, upper_limit)

    return json.dumps(random_list)

if __name__ == '__main__':
    app.run()