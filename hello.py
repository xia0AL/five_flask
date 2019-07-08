from flask import Flask, request, make_response
from flask import render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/unsafe/cwe116')
def unsafe_cwe116():
    first_name = request.args.get('name')
    return str(first_name)

@app.route('/unsafe/pickle')
def unsafe_pickle():
    user = request.args.get('userpickled')
    user_obj = pickle.loads(user)
    return "unsafe pickle example"

if __name__ == "__main__":
    app.run(debug=True)
