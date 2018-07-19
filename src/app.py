from flask import Flask

app = Flask(__name__)

@app.rout('/')
def home():
    return "Hello World"

# @app.route('/') by default is a get request

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name', methods=['GET'])
def get_store_name(name):
    pass

# GET /store
@app.route('/store', methods=['GET'])
def get_store():
    pass

# POST /store/<string:name/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    pass

# GET /store/<string:name/item
@app.route('/store/<string:name>/item', method=['GET'])
def get_store_item():
    pass

app.run(port=5080)