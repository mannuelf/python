from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.rout('/')
def home():
    return "Hello World"

stores = [
    {
        'name': 'MannuelShops',
        'items': [
            {
                'name': 'Google Nexus',
                'price': 399.99
            }
        ]
    }
]

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
    return jsonify({'stores': stores})

# POST /store/<string:name/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    pass

# GET /store/<string:name/item
@app.route('/store/<string:name>/item', method=['GET'])
def get_store_item():
    pass

app.run(port=5080)