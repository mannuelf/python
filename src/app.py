from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
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
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store_name(name):
    pass

# GET /store
@app.route('/store', methods=['GET'])
def get_store():
    return jsonify({'stores': stores})

# POST /store/<string:name/item
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_store_item(name):
#     pass

# GET /store/<string:name/item
# @app.route('/store/<string:name>/item', method=['GET'])
# def get_store_item(name):
#     pass

app.run(port=5080)