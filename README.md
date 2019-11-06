# thermos
**Experiments with a Python's Flask based web server.**
![](https://cdn.pixabay.com/photo/2018/08/28/20/21/jug-3638398_960_720.jpg)

This tiny project shows how to build RESTful APIs with Flask. You can define endpoints and the code that needs to be executed when invoked. You can send messages via the REST API and act on it in your Python code.

## Quickstart
### Creating your dev env
To run, first clone this repo and enter its folder in terminal. Then clone  the dev env using the `requirements.txt` file. To do so first create a conda env by running:
```
conda create env --name flask2 python
```
then install the dependencies by running:
```
pip install -r requirements.txt
```

### Running this project
All endpoints are defined in a single `app.py` which is what should be run by the web server. After you activate and install the dependencies, from the terminal run:

```
python -m app
```
which will start the web server and give you an address to hit. There is a simple HTML frontpage that you can use as UI or you can interact with the REST endpoints programmatically.


## Publishing to Heroku
These are the general steps

1. Install all dependencies using `pip` as conda support is not matured yet.
2. Freeze dependencies using `pip freeze -r requirements.txt`
3. Create a `Procfile` with contents `web: gunicorn app:app`. Here we switch from Flask server to Gunicorn which is a light weight, but production ready server.
4. Install Heroku CLI, create an account, make keys, login to client.
5. Create Heroku app as `heroku apps:create atma-thermos`. Note: you need to name it differently as the name I chose is taken by me.
6. Test locally using `heroku local web`.
7. Commit your changes. Push to both remotes.
```git

```