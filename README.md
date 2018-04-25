# thermos
Experiments with a Python's Flask based web server.

This tiny project shows how to build RESTful APIs with Flask. You can define endpoints and the code that needs to be executed when invoked. You can send messages via the REST API and act on it in your Python code.

### Creating your dev env
To run, first clone the dev env using the `environment.yml` file. To do so, run:
```
conda create --file environment.yml
```

### Running this project
Then to run the web server run this the first time (you are setting which file needs to be executed when Flask is called):
```
export FLASK_APP = thermos.py
```
and to start the web server, run:
```
python -m flask run
```
Then open your browser on the IP address flask prints on terminal, usually it is `127.0.0.1:5000`. After you update the Python files, stop and restart the server for changes to take effect.
