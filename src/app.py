from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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
    for store in stores: # Iterate over steps
        if store['name'] == name: # If t he store name matches, return it
            return jsonify(store)
    return jsonify({'message': 'store not found'}) # If none match, return an error message

# GET /store
@app.route('/store', methods=['GET'])
def get_store():
    return jsonify({'stores': stores})

# POST /store/<string:name/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_store_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'stores not found'})

app.run(port=5080)