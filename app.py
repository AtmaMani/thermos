# region imports
from flask import Flask
app = Flask(import_name=__name__)

# import to parse wildcard args
from flask import request

# import to render html pages
from flask import render_template

# to handle errors and reload the same resource
from flask import redirect

# to flash messages on screen
from flask import flash

# to return files over web
from flask import send_from_directory

# other imports
import json
from executor import generate_unique_random_integers
from geocode_tool import geocode_address_executor
import os, sys, socket
from roti_rot import rot13
import requests
# end region

# region startup routine
with open('xrl.txt', 'r') as read_handle:
    key = rot13(read_handle.readline())
# end region

# define the root resource
@app.route('/', methods=['GET'])
def index_page():
    try:
        mac_ip = socket.gethostbyname(socket.gethostname())
    except:
        mac_ip = None
    return render_template('index.html',
                           sys_path = str(sys.path),
                           os_type = str(sys.platform),
                           os_name = str(os.name),
                           mac_name = str(socket.gethostname()),
                           mac_ip=mac_ip)

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

@app.route('/geocodeAddress', methods=['GET'])
def geocode_address():
    """
    Called as /geocodeAddress?address="123 Main St, City, State"
    :return:
    """
    address = request.args.get('address', '380 New York St, Redlands, CA')
    geocode_dict = geocode_address_executor(address)
    return json.dumps(geocode_dict)

@app.route('/eyeFromAbove', methods=['GET', 'POST'])
def eye_from_above():
    """
    If GET request - Displays a html page with box to enter address
    if POST request - renders output html with image from above
    :return:
    """
    if request.method == 'POST':
        # User could have used the web UI or called the endpoint headless

        # If user used the web UI, then address comes as form data
        if request.form is not None:
            address = request.form.get('address', None)
            date = request.form.get('date', None)
        else:
            # request data comes via args
            address = request.args.get('address', None)
            date = request.args.get('date', None)
        if address:
            geocode_dict = geocode_address_executor(address)
            lon = geocode_dict['location']['x']
            lat = geocode_dict['location']['y']

        else: # when no address is loaded
            flash('No address specified')
            return redirect(request.url)

        base_url = 'https://api.nasa.gov/planetary/earth/imagery'
        params = {'lat':lat,
                  'lon':lon,
                  'dim':0.025,
                  'date':date,
                  'cloud_score':False,
                  'api_key':key
                  }

        # for some reason, NASA server rejects the GET request if I send data over payload
        if date:
            full_url = f'{base_url}/?lat={lat}&lon={lon}&date={date}&cloud_score=False&api_key={key}'
        else:
            full_url = f'{base_url}/?lat={lat}&lon={lon}&cloud_score=False&api_key={key}'


        # construct the query and get download url
        # resp = requests.get(base_url, params)
        resp = requests.get(full_url)

        if resp.status_code == 200:
            resp_dict = json.loads(resp.text)
        else:
            return json.dumps({'error':resp.text})

        # Download the image from Google Earth Engine API.
        img_resp = requests.get(resp_dict['url'])
        if img_resp.status_code == 200:
            img_filename = address.replace(' ','_').replace('-','').replace('.','').replace('*','').replace(',','')
            with open(f'eye_in_sky_queries/{img_filename}.png', 'wb') as img_handle:
                img_handle.write(img_resp.content)
        else:
            return json.dumps({'error':img_resp.text})

        # render the HTML page
        return render_template('eye_from_above.html',
                               media_type='image',
                               media_url = os.path.join('/','eye_in_sky_queries',img_filename+'.png'),
                               img_date = resp_dict['date'],
                               img_id = resp_dict['id'],
                               img_dataset = resp_dict['resource']['dataset'])

    elif request.method == 'GET':
        # case when page is loaded on browser
        return '''
            <!doctype html>
            <title>Enter address to view</title>
            <h1>Enter the address to get image of</h1>
            <form method=post enctype=multipart/form-data>
              <input type=text name=address value=address>
              <input type=text name=date value='2013-12-17'>
              <input type=submit value=Submit>
            </form>
            '''

# this resource is needed for the HTML page to display the image that is downloaded
@app.route('/eye_in_sky_queries/<filename>')
def uploaded_file(filename):
    return send_from_directory('eye_in_sky_queries',
                               filename)

if __name__ == '__main__':
    app.run()