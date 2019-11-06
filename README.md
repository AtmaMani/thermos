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
